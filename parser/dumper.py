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

    @visitor(LogicalOperator)
    def visit(self, logop):
        # Always use parentheses to reflect grouping and associativity, even if they may
        # be superfluous.
        return "(%s %s %s)" % (logop.left.accept(self), logop.op, logop.right.accept(self))

    @visitor(IfThenElse)
    def visit(self, ite):
        return "(if %s then %s else %)" % (ite.condition.accept(self),
                                           ite.then_part.accept(self),
                                           ite.else_part.accept(self))
    @visitor(Identifier)
    def visit(self, id):
        return id.name
