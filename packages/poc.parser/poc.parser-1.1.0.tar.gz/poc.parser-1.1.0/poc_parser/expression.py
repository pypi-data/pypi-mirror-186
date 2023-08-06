import ast
import sys
import sre_compile
import functools

from .gtlog import GTLog
from .utils import *
from .thirdparty_packages.requests.models import Response


class ExpressionParser(ast.NodeVisitor):

    _boolean_ops = {
        ast.And: lambda left, right: left and right,
        ast.Or: lambda left, right: left or right
    }

    _binary_ops = {
        ast.Add: lambda left, right: left + right,
        ast.Sub: lambda left, right: left - right,
        ast.Mult: lambda left, right: left * right,
        ast.Div: lambda left, right: left / right,
        ast.Mod: lambda left, right: left % right,
        ast.Pow: lambda left, right: left ** right,
        ast.LShift: lambda left, right: left << right,
        ast.RShift: lambda left, right: left >> right,
        ast.BitOr: lambda left, right: left | right,
        ast.BitXor: lambda left, right: left ^ right,
        ast.BitAnd: lambda left, right: left & right,
        ast.FloorDiv: lambda left, right: left // right
    }

    # Unary operators
    _unary_ops = {
        ast.Invert: lambda operand: ~operand,
        ast.Not: lambda operand: not operand,
        ast.UAdd: lambda operand: +operand,
        ast.USub: lambda operand: -operand
    }

    # Comparison operators
    # The AST nodes may have multiple ops and right comparators, but we
    # evaluate each op individually.
    _compare_ops = {
        ast.Eq: lambda left, right: left == right,
        ast.NotEq: lambda left, right: left != right,
        ast.Lt: lambda left, right: left < right,
        ast.LtE: lambda left, right: left <= right,
        ast.Gt: lambda left, right: left > right,
        ast.GtE: lambda left, right: left >= right,
        ast.Is: lambda left, right: left is right,
        ast.IsNot: lambda left, right: left is not right,
        ast.In: lambda left, right: left in right,
        ast.NotIn: lambda left, right: left not in right
    }

    # Predefined variable names
    _variable_names = {
        'True': True,
        'False': False,
        'None': None
    }

    # Predefined functions
    _function_names = {
        'int': int,
        'float': float,
        'bool': bool,
        'str': str,
        'bytes': convert_bytes,
        'md5': md5,
        'rand': rand,
        'len': lambda a: len(a),
        'randint': randint,
        'b64encode': b64encode,
        'b64decode': b64decode,
        'tcp': tcp,
        'udp': udp
    }

    def __init__(self, variables=None, proxies=None):
        self._variables = variables or {}
        self._proxies = proxies or {}
        self.last_ret = []  # 最后一次表达式运行返回值[True, False]
        self._gtlog = GTLog()

    @property
    def response(self):
        return self._variables.get("response", None)

    @response.setter
    def response(self, response):
        if isinstance(response, Response):
            self._variables["response"] = response
            self._variables["request"] = response.request
        else:
            self._variables["response"] = self._variables["request"] = None

    def parse(self, expression):
        """
        Parse a string `expression` and return its result.
        """
        self.last_ret = []  # 清空返回值
        try:
            return self.visit(ast.parse(expression))
        except SyntaxError as error:
            error.text = expression
            raise error
        except Exception as error:
            raise error

    @property
    def variables(self):
        """
        Retrieve the variables that exist in the scope of the parser.

        This property returns a copy of the dictionary.
        """

        return self._variables

    def add_variable(self, **kwargs):
        self._variables.update(kwargs)

    def visit_Module(self, node):
        """
        Visit the root module node.
        """
        if len(node.body) != 1:
            if len(node.body) > 1:
                lineno = node.body[1].lineno
                col_offset = node.body[1].col_offset
            else:
                lineno = 1
                col_offset = 0

            raise SyntaxError('Exactly one expression must be provided',
                              ('', lineno, col_offset, ''))

        return self.visit(node.body[0])

    def visit(self, node):
        """Visit a node."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        # print("[*]", method, visitor, node)
        return visitor(node)

    def visit_Expr(self, node):
        """
        Visit an expression node.
        """
        return self.visit(node.value)

    def visit_BoolOp(self, node):
        """
        Visit a boolean expression node.
        """

        op = type(node.op)
        func = self._boolean_ops[op]
        result = func(self.visit(node.values[0]), self.visit(node.values[1]))
        for value in node.values[2:]:
            result = func(result, self.visit(value))

        return result

    def visit_BinOp(self, node):
        """
        Visit a binary expression node.
        """

        op = type(node.op)
        func = self._binary_ops[op]
        return func(self.visit(node.left), self.visit(node.right))

    def visit_UnaryOp(self, node):
        """
        Visit a unary expression node.
        """

        op = type(node.op)
        func = self._unary_ops[op]
        return func(self.visit(node.operand))

    def visit_Compare(self, node):
        """
        Visit a comparison expression node.
        """

        result = self.visit(node.left)
        for operator, comparator in zip(node.ops, node.comparators):
            op = type(operator)
            func = self._compare_ops[op]
            result = func(result, self.visit(comparator))

        return result

    def visit_keyword(self, node):
        """
        Visit a funtion **kwargs
        """
        return node.arg, self.visit(node.value)

    def visit_Call(self, node):
        """
        Visit a function call node.
        """
        if isinstance(node.func, ast.Name):
            name = node.func.id
            if name == "get_domain":
                return self._gtlog.get_random_domain()
            elif name == "verify_dnslog":
                return self._gtlog.verify_dnslog()
            elif name == "get_ldap_payload":
                return self._gtlog.get_ldap_payload()
            elif name == "verify_ldaplog":
                return self._gtlog.verify_ldaplog()
            elif name == "invoke_jar":
                func = functools.partial(invoke_jar, proxies=self._proxies)
            elif name in self._function_names:
                func = self._function_names[name]
            else:
                raise NameError("Function '{}' is not defined".format(name),
                                node.lineno, node.col_offset)
        elif isinstance(node.func, ast.Attribute):
            func = self.visit(node.func)
        else:
            raise SyntaxError("node function is not valid")

        args = [self.visit(arg) for arg in node.args]
        keywords = dict([self.visit(keyword) for keyword in node.keywords])

        ret = func(*args, **keywords)
        if isinstance(ret, type(sre_compile.compile('', 0).match(''))):
            self.add_variable(**ret.groupdict())  # 记录正则匹配结果
        self.last_ret.append(ret)  # 记录返回值
        return add_extra_method(ret)

    def visit_Assign(self, node):
        kwargs = {}
        value = self.visit(node.value)
        if isinstance(node.targets[0], ast.Tuple):
            # 多个赋值
            if len(value) != len(node.targets[0].elts):
                raise SyntaxError(f"Variables({len(node.targets[0].elts)}) != values({len(value)}), assign failed")
            for i, v in enumerate(value):
                kwargs[node.targets[0].elts[i].id] = v
        else:
            # 单一赋值
            kwargs[node.targets[0].id] = value
        self.add_variable(**kwargs)

    def visit_IfExp(self, node):
        if self.visit(node.test):
            return self.visit(node.body)
        else:
            return self.visit(node.orelse)

    def visit_Num(self, node):
        return node.n

    def visit_Tuple(self, node):
        params = []
        for n in node.elts:
            params.append(self.visit(n))
        return tuple(params)

    def visit_Name(self, node):
        """
        Visit a named variable node.
        """
        if node.id in self._variables:
            return add_extra_method(self._variables[node.id])

        if node.id in self._variable_names:
            return self._variable_names[node.id]

        raise NameError("Name '{}' is not defined".format(node.id),
                        node.lineno, node.col_offset)

    def visit_Attribute(self, node: ast.Attribute):
        if node.attr.startswith("__"):
            raise SyntaxError(f'Can not access `{node.attr}` attribute')
        attr = getattr(self.visit(node.value), node.attr)
        return add_extra_method(attr)

    def visit_Str(self, node):
        return Customstr(node.s)

    def visit_Bytes(self, node):
        return Custombytes(node.s)

    def visit_Subscript(self, node):
        name = self.visit(node.value)
        if isinstance(node.slice, ast.Slice):
            lower = self.visit(node.slice.lower) if node.slice.lower else None
            upper = self.visit(node.slice.upper) if node.slice.upper else None
            step = self.visit(node.slice.step) if node.slice.step else None
            return add_extra_method(name[lower: upper: step])
        if isinstance(node.slice, ast.Constant):
            # python >=3.9
            index = node.slice.value
        elif isinstance(node.slice, ast.Index):
            # python < 3.9
            index = self.visit(node.slice.value)
        else:
            raise RuntimeError(f"Unsupported python version: {sys.version}")
        try:
            return add_extra_method(name[index])
        except KeyError:
            # 访问不存在的字典属性返回空值
            return add_extra_method("")
