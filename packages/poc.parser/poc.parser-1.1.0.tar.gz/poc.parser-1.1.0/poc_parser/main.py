import json
from copy import deepcopy
import http.client
from typing import *
from urllib.parse import urlparse

import yaml

from .gtlog import GTLog
from .expression import ExpressionParser, SnapShot, Socket
from .thirdparty_packages import requests


class PocArgs(object):
    """
    poc 规则单个 uri 参数
    """
    def __init__(self, jdata: Dict) -> None:
        """
        构造
        """
        self.uri = jdata.get('uri', None)
        self.uriencode = jdata.get('uriencode', True)
        self.method = jdata.get('method', 'GET')
        self.headers = jdata.get('headers', {})
        self.body: str = jdata.get('body', '')
        self.allow_redirects: bool = jdata.get("allow_redirects", True)
        self.assign: str = str(jdata.get('assign', ''))
        self.expression: str = str(jdata.get('expression', ''))
        self.loop_option: dict = jdata.get('loop_option', {})
        self.timeout = jdata.get('timeout', 15)
        self.size_limit = jdata.get('size_limit', 0)

        # 文件上传漏洞body内有的服务器不认\n分隔符, 这个分支把\n替换为\r\n
        if "multipart/form-data" in self.headers.get("Content-Type", "") and self.body:
            str_list = list(self.body)
            for index in range(1, len(str_list)):
                if str_list[index - 1] != "\r" and str_list[index] == "\n":
                    str_list.insert(index, "\r")
            self.body = "".join(str_list)

    def __repr__(self):
        return str(self.__dict__)


class PocRule(object):  # pylint: disable=too-many-instance-attributes
    """
    从路径或字典初始化poc 规则
    """
    def __init__(self, relativepath: str, debug=False, proxies=None, jdata=None) -> None:
        """
        构造
        """
        # 运行日志
        self.running_log = []

        self.debug = debug
        if isinstance(jdata, dict):
            jdata = jdata
        else:
            path = relativepath.replace(".", "/")
            path = path if path.endswith(".yml") else path + ".yml"
            with open(path, encoding="utf-8") as f:
                jdata = yaml.safe_load(f)

        # 信息参数
        self.product = jdata.get("product", '')
        self.name = jdata.get('name', '')
        self.holetype = jdata.get('holetype', 'other')
        self.level = jdata.get('level', None)

        self.desc = jdata.get('desc', '')
        self.author = jdata.get('author', '')

        # 规则参数
        self.poc_args = [PocArgs(poc_args) for poc_args in jdata.get('rules', [])]

        # 可选参数
        self.control = jdata.get('control', 'SEQ')  # 多个rule之间逻辑 SEQ/AND/OR
        self.http_version = jdata.get('http_version', "1.1")  # HTTP版本
        http.client.HTTPConnection._http_vsn_str = f"HTTP/{self.http_version}"
        self.set = jdata.get('set', {})  # 变量预定义
        self.ret = jdata.get('ret', f'检测到 {self.name}, {self.desc}')  # 命中后返回内容

        # 表达式解析器
        self._parser = None

        # 记录poc运行时的产生的结果
        self._snapshots: [SnapShot] = []

        self.proxies = proxies if proxies else {}
        self.session = requests.Session()

        # 初始化dnslog
        self.gtlog = GTLog()

    def __repr__(self) -> str:
        return str(self.__dict__)

    @property
    def parser(self):
        if not self._parser:
            self._parser = ExpressionParser(proxies=self.proxies)
        return self._parser

    @property
    def snapshots(self):
        # _snapshot内的值最后才混合tcp数据，时序可能不对，这里排个序
        return [s.to_dict() for s in sorted(self._snapshots, key=lambda k: k.start_time)]

    @staticmethod
    def __get_host(url):
        return urlparse(url).hostname

    @staticmethod
    def __get_port(url):
        parse_result = urlparse(url)
        if parse_result.port:
            return parse_result.port
        else:
            if parse_result.scheme == "http":
                return 80
            elif parse_result.scheme == "https":
                return 443
            else:
                return 0

    def __find_vars(self, poc_string, result=None) -> [bytes or str]:
        if result is None:
            result = []
        if isinstance(poc_string, bytes):
            start = poc_string.find(b"{{")
            end = poc_string.find(b"}}")
        else:
            start = poc_string.find("{{")
            end = poc_string.find("}}")
        if end > start > -1:
            result.append(poc_string[start: end + 2])
            self.__find_vars(poc_string[:start] + poc_string[end+2:], result)
        return result

    def __replace_vars(self, args):
        args_type = "byte" if isinstance(args, bytes) else "str"
        for var in self.__find_vars(args):
            if args_type == "byte":
                var_name = var.strip(b"{} ")
            else:
                var_name = var.strip("{} ")
            var_value = self.parser.parse(var_name)  # 解析表达式
            if isinstance(var_value, bytes):
                args = args.replace(var, var_value)
            else:
                args = args.replace(var, str(var_value))
        return args

    def __init_set(self):
        # 初始化poc中的set变量
        for k, expression in self.set.items():
            if isinstance(expression, str):
                value = self._parser.parse(expression)
            elif isinstance(expression, list):
                value = expression
            else:
                raise RuntimeError(f"Wrong parameter: {expression}")
            self.parser.add_variable(**{k: value})

    def __request(self, url, poc_args: PocArgs):
        resp = self.session.request(
            method=poc_args.method,
            url=f'{url}{poc_args.uri}',
            headers=poc_args.headers,
            data=poc_args.body,
            allow_redirects=poc_args.allow_redirects,
            timeout=poc_args.timeout,
            proxies=self.proxies,
            uriencode=poc_args.uriencode,
            stream=True
        )
        if poc_args.size_limit > 0:
            content, size_temp = b"", 0
            for chunk in resp.iter_content():
                if chunk:
                    size_temp += len(chunk)
                    content += chunk
                    if size_temp >= poc_args.size_limit:
                        break
            resp.close()
            resp._content = content
        return resp

    def _exec_single_rules(self, url, poc_args: PocArgs) -> bool or None:
        # 替换表达式参数
        if poc_args.loop_option:
            return self._execute_loop_rules(url, poc_args)
        poc_args.uri = self.__replace_vars(poc_args.uri)
        poc_args.body = self.__replace_vars(poc_args.body)
        for k in poc_args.headers:
            poc_args.headers[k] = self.__replace_vars(poc_args.headers[k])

        # 执行请求和表达式
        resp = None
        if poc_args.uri is not None:
            resp = self.__request(url, poc_args)
            self.parser.response = resp
            self.log(requests.dump_all(resp))

        save_snapshot = False
        ret = None
        if poc_args.assign:
            self.parser.parse(poc_args.assign)
            save_snapshot = True
        if poc_args.expression:
            ret = bool(self.parser.parse(poc_args.expression))
            if ret:
                save_snapshot = True
        if save_snapshot and resp:
            self._save_snapshot(resp)
        return ret

    def __build_req_list(self, poc_args: PocArgs) -> [PocArgs]:
        uri, body, headers = [], [], []
        poc_args_list = []
        # 带大括号的变量名
        var_in_uri = self.__find_vars(poc_args.uri)
        var_in_body = self.__find_vars(poc_args.body)
        var_in_headers = []
        for value in poc_args.headers.values():
            var_in_headers += self.__find_vars(value)
        # 记录变量名对应的值
        var_value = {}
        for name in var_in_uri + var_in_body + var_in_headers:
            value = self.parser.parse(name.strip("{} "))
            var_value[name] = value
        mode = poc_args.loop_option.get("mode")
        # 约束校验
        if mode == "1-for-1":
            first_length = None
            for v in var_value.values():
                if isinstance(v, list):
                    if first_length is None:
                        first_length = len(v)
                    else:
                        try:
                            assert first_length == len(v)
                        except AssertionError:
                            raise RuntimeError("1-for-1 variable should have same length ")
            # 生成请求列表
            for idx in range(0, first_length):
                new_poc_args = deepcopy(poc_args)
                for var_name in var_in_uri:
                    value = var_value[var_name][idx] if isinstance(var_value[var_name], list) else var_value[var_name]
                    new_poc_args.uri = new_poc_args.uri.replace(var_name, value)
                for var_name in var_in_body:
                    value = var_value[var_name][idx] if isinstance(var_value[var_name], list) else var_value[var_name]
                    new_poc_args.body = new_poc_args.body.replace(var_name, value)
                for var_name in var_in_headers:
                    value = var_value[var_name][idx] if isinstance(var_value[var_name], list) else var_value[var_name]
                    for k, v in new_poc_args.headers.items():
                        new_poc_args.headers[k] = v.replace(var_name, value)
                poc_args_list.append(new_poc_args)
        else:
            req = {"uri": [poc_args.uri], "body": [poc_args.body], "headers": [json.dumps(poc_args.headers)]}
            for part in req.keys():
                poc_string = req[part]
                for var_name in locals()[f"var_in_{part}"]:
                    new_item = []
                    for u in poc_string:
                        values = var_value[var_name]
                        if isinstance(values, list):
                            for value in values:
                                new_item.append(u.replace(var_name, value))
                        else:
                            new_item.append(u.replace(var_name, values))
                        poc_string = new_item
                req[part] = poc_string
            for uri in req["uri"]:
                for body in req["body"]:
                    for headers in req["headers"]:
                        new_poc_args = deepcopy(poc_args)
                        new_poc_args.uri = uri
                        new_poc_args.body = body
                        new_poc_args.headers = json.loads(headers)
                        poc_args_list.append(new_poc_args)
        return poc_args_list

    def _execute_loop_rules(self, url, poc_args: PocArgs):
        req_list: [PocArgs] = self.__build_req_list(poc_args)
        flag = False
        for req in req_list:
            ret = None
            save_snapshot = False
            resp = self.__request(url, req)
            self.parser.response = resp
            self.log(requests.dump_all(resp))
            if poc_args.assign:
                self.parser.parse(poc_args.assign)
                save_snapshot = True
            if poc_args.expression:
                ret = bool(self.parser.parse(poc_args.expression))
                if ret:
                    flag = True
                    save_snapshot = True
            if save_snapshot:
                self._save_snapshot(resp)
            if ret and poc_args.loop_option.get("stop-at-first-match", True):
                return ret
        return flag

    def _save_snapshot(self, response):
        snapshot = SnapShot()
        snapshot.send = requests.dump_request(response)
        snapshot.recv = requests.dump_response(response)
        self._snapshots.append(snapshot)

    def execute(self, url, headers: dict = None):
        if headers is not None:
            for k, v in headers.items():
                self.session.headers[k] = v
        result = {"status": False}
        # 初始化运行过程中变量
        self.parser.add_variable(url=url, host=self.__get_host(url), port=self.__get_port(url))
        self.__init_set()

        if self.proxies:
            self.log(f"正在使用代理: {self.proxies}")

        expression_results = []

        for i, poc_args in enumerate(self.poc_args):
            exp_result = self._exec_single_rules(url, poc_args)

            self.log(f"函数解析结果: {self.parser.last_ret}")
            self.log(f"表达式解析结果: {exp_result}")
            self.log(f"当前可用变量：{self.parser.variables}")

            if exp_result is not None:  # 没有表达式返回None，不参与逻辑判断，仅赋值使用
                expression_results.append(exp_result)
                if self.control == "OR" and exp_result is True:
                    # OR规则只需要有一个为真即跳出检测
                    break
                if self.control != "OR" and exp_result is False:
                    # AND, SEQ规则只需要有一个为假即跳出检测
                    break

        # 判断是否命中
        if self.control == "OR":
            result["status"] = any(expression_results)
        else:
            result["status"] = all(expression_results)

        for _, var in self.parser.variables.items():
            # 先凑合用，等全部运行完毕后一次获取全部数据包，避免处处回参传参，太麻烦
            if isinstance(var, Socket):
                self._snapshots += var.snapshots

        if result["status"]:
            result["ret"] = self.__replace_vars(self.ret)

        self.log("*" * 10)
        self.log(f"检测结果：{result}")
        return result

    def log(self, *args):
        for arg in args:
            if isinstance(arg, dict):
                arg = json.dumps(arg, indent=2)
            self.running_log.append(arg)
            if self.debug:
                print(arg)
