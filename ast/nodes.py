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
