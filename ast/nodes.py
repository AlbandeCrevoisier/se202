#
# This file contains the definition of the nodes used in the Tiger
# project. It must not be modified.
#


class Node:
    """The Node type represents a node in the AST. Its notable fields are:
      - children: a list of children to visit when visiting the AST and no
                  treatment has been given for this kind of node.
    """

    def __init__(self):
        self.children = []
        self.type = None

    def accept(self, visitor):
        return visitor.visit(self)


class IntegerLiteral(Node):

    def __init__(self, intValue):
        super().__init__()
        self.intValue = intValue


class BinaryOperator(Node):

    def __init__(self, op, left, right):
        super().__init__()
        self.op = op
        self.left = left
        self.right = right
        self.children = [left, right]


class Let(Node):

    def __init__(self, decls, exps):
        super().__init__()
        self.decls = decls
        self.exps = exps
        self.children = decls + exps


class Identifier(Node):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.decl = None


class IfThenElse(Node):

    def __init__(self, condition, then_part, else_part):
        super().__init__()
        self.condition = condition
        self.then_part = then_part
        self.else_part = else_part
        self.children = [condition, then_part, else_part]


class Type(Node):

    def __init__(self, typename):
        super().__init__()
        self.typename = typename


class Decl(Node):
    """Abstract type regrouping various entity declarations"""

    def __init__(self):
        super().__init__()
        self.escapes = False
        self.depth = None


class VarDecl(Decl):

    def __init__(self, name, type, exp):
        super().__init__()
        self.name = name
        self.type = type
        self.exp = exp
        self.children = [type, exp]


class FunDecl(Decl):

    def __init__(self, name, args, type, exp):
        super().__init__()
        self.name = name
        self.args = args
        self.type = type
        self.exp = exp
        self.children = args + [type, exp]


class FunCall(Node):

    def __init__(self, identifier, params):
        super().__init__()
        self.identifier = identifier
        self.params = params
        self.children = params
