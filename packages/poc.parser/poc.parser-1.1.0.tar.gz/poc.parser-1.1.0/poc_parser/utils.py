import hashlib
import re
import time
import os
import random
import socket
import string
import subprocess
import base64


class SnapShot(object):
    def __init__(self):
        self._start_time = time.time()
        self._end_time = None
        self._send = ""
        self._recv = ""

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def send(self):
        return self._send

    @property
    def recv(self):
        return self._recv

    @send.setter
    def send(self, value):
        self._send = value
        self._end_time = time.time()

    @recv.setter
    def recv(self, value):
        self._recv = value
        self._end_time = time.time()

    def to_dict(self):
        return {
            "start_time": self._start_time,
            "end_time": self._end_time,
            "send": self._send,
            "recv": self._recv
        }

    def __lt__(self, other):
        return self._start_time > other.start_time

    def __repr__(self):
        return str(self.to_dict())


class Custombytes(bytes):
    def contains(self, a, encoding="utf-8"):
        if isinstance(a, str):
            return a in self.decode(encoding)
        elif isinstance(a, bytes):
            return a in self
        else:
            raise SyntaxError("`contains` method argument must be str or bytes")

    def match(self, a, encoding="utf-8"):
        if isinstance(a, str):
            pattern = re.compile(a)
            ret = re.search(pattern, self.decode(encoding))
        elif isinstance(a, bytes):
            pattern = re.compile(a)
            ret = re.search(pattern, self)
        else:
            raise SyntaxError("`match` method argument must be str or bytes")
        return ret if ret else False


class Customstr(str):
    def contains(self, a, encoding="utf-8"):
        if isinstance(a, str):
            return a in self
        elif isinstance(a, bytes):
            return a in self.encode(encoding)
        else:
            raise SyntaxError("`contains` method argument must be str or bytes")

    def match(self, a, encoding="utf-8"):
        if isinstance(a, str):
            pattern = re.compile(a)
            ret = re.search(pattern, self)
        elif isinstance(a, bytes):
            pattern = re.compile(a)
            ret = re.search(pattern, self.encode(encoding))
        else:
            raise SyntaxError("`match` method argument must be str or bytes")
        return ret if ret else False


def add_extra_method(s):
    if isinstance(s, str):
        return Customstr(s)
    elif isinstance(s, bytes):
        return Custombytes(s)
    else:
        return s


def md5(x):
    if isinstance(x, str):
        x = x.encode("utf-8")
    return hashlib.md5(x).hexdigest()


def rand(length, _type="all"):
    if _type == "lowercase":
        s = string.ascii_lowercase
    elif _type == "uppercase":
        s = string.ascii_uppercase
    elif _type == "int":
        s = string.digits
    elif _type == "all":
        s = string.ascii_letters + string.digits
    else:
        raise SyntaxError("type must be `lowercase, uppercase, int, all`")
    return ''.join(random.sample(s, length))


def randint(x, y):
    return random.randint(x, y)


def convert_bytes(s, encoding="utf-8"):
    if not isinstance(s, str):
        s = str(s)
    return s.encode(encoding)


def b64encode(s):
    if isinstance(s, str):
        s = s.encode("utf-8")
    return base64.b64encode(s)


def b64decode(s):
    return base64.b64decode(s)


def invoke_jar(jar_path, *args, proxies=None, timeout=120):
    """
    :param jar_path: java程序路径
    :param args: java参数
    :param proxies: 是否使用代理{"http:": "", "https:": ""}
    :param timeout: 默认超时时间
    :return:
    """
    if not os.path.isfile(jar_path):
        jar_path = os.path.join("plugins", "poc_yml", jar_path)
    cmd = ["java", "-jar", jar_path, *args]
    if proxies:
        cmd = ["proxychainwrap.sh", "-n", proxies["http"]] + cmd
    try:
        proc = subprocess.run(cmd, timeout=timeout, capture_output=True)
    except subprocess.TimeoutExpired:
        return Customstr("")
    except FileNotFoundError:
        return Customstr("`Cannont found java in PATH, please install jdk first`")
    if proc.returncode == 0:
        return Custombytes(proc.stdout)
    else:
        return Custombytes(proc.stderr)


class Socket(object):
    def __init__(self, host, port, timeout, protocol):
        self.host = host
        self.port = int(port)
        self.timeout = int(timeout)
        self.protocol = protocol
        self.open = False
        # 记录数据流{"direct": "send", "data": "", "time": timestamp}
        self.stream = []
        if protocol == "tcp":
            # 不处理异常，出现异常就报错退出，让上层应用处理
            self.sock = socket.create_connection((host, int(port)), timeout=timeout)
            self.stream.append({"direct": "send", "data": f"Connected to {host}:{port} over TCP.", "time": time.time()})
        else:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.settimeout(timeout)
            self.stream.append({"direct": "send", "data": f"Ready sendto {host}:{port} over UDP.", "time": time.time()})
        # 没有异常为open
        self.open = True

    @property
    def snapshots(self) -> [dict]:
        # stream convert snapshot
        snapshots = []
        # 第一个是连接信息
        packet = self.stream.pop(0)
        new_snapshot = SnapShot()
        new_snapshot.send = packet["data"]
        new_snapshot._start_time = new_snapshot._end_time = packet["time"]
        snapshots.append(new_snapshot)
        stack = []
        for packet in self.stream:
            if packet["direct"] == "send":
                stack.append(packet)
            else:
                # 匹配到回包，创建一个快照
                new_snapshot = SnapShot()
                new_snapshot.send = " ".join([p["data"] for p in stack])
                new_snapshot.recv = packet["data"]
                if stack:  # 处理没有发送过包的边界情况
                    new_snapshot._start_time = stack[0]["time"]
                else:
                    new_snapshot._start_time = packet["time"]
                new_snapshot._end_time = packet["time"]
                snapshots.append(new_snapshot)
                stack.clear()
        if len(stack) > 0:
            # 栈不空，有剩余的请求，但没调用过recv, 也创建一个快照
            new_snapshot = SnapShot()
            new_snapshot.send = " ".join([p["data"] for p in stack])
            new_snapshot._start_time, new_snapshot._end_time = stack[0]["time"], stack[-1]["time"]
            snapshots.append(new_snapshot)
            stack.clear()
        return snapshots

    def send(self, data):
        if isinstance(data, str):
            data = data.encode()
        if self.protocol == "tcp":
            self.sock.send(data)
        else:
            self.sock.sendto(data, (self.host, self.port))
        self.stream.append({"direct": "send", "time": time.time(), "data": data.decode("latin1")})
        return True

    def recv(self, length=4096):
        try:
            data = self.sock.recv(length)
            self.stream.append({"direct": "recv", "time": time.time(), "data": data.decode("latin1")})
            return Custombytes(data)
        except socket.timeout:
            return Custombytes(b"")

    def close(self):
        try:
            self.sock.close()
        except:
            pass

    def __repr__(self):
        return self.sock.__repr__()

    def __str__(self):
        return self.sock.__str__()


def tcp(host, port, timeout=5):
    return Socket(host, port, timeout, "tcp")


def udp(host, port, timeout=5):
    return Socket(host, port, timeout, "udp")