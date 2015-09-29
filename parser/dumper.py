from ast.nodes import *
from utils.visitor import *

class Dumper(Visitor):

    @visitor(None)
    def visit(self, node):
        raise Exception("unable to dump %s" % node)

    @visitor(IntegerLiteral)
    def visit(self, i):
        return str(i.intValue)

    @visitor(BinaryOperator)
    def visit(self, binop):
        # Always use parentheses to reflect grouping and associativity, even if they may
        # be superfluous.
        return "(%s %s %s)" % (binop.left.accept(self), binop.op, binop.right.accept(self))

    @visitor(Identifier)
    def visit(self, id):
        return id.name
