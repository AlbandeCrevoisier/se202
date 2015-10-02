from ast.nodes import *
from utils.visitor import visitor

class Evaluator:
    """This contains a simple evaluator visitor which computes the value
    of a tiger expression."""

    @visitor(IntegerLiteral)
    def visit(self, int):
        return int.intValue

    @visitor(BinaryOperator)
    def visit(self, binop):
        left, right = binop.left.accept(self), binop.right.accept(self)
        op = binop.op
        if op == '+':
            return left + right
        elif op == '*':
            return left * right
        elif op == '-':
            return left - right 
        elif op == '/':
            return left // right 
        # True = 1, False = 0
        # thus left * right would be right, but not readable. Possible optim ?
        elif op == '&':
            if left == 1 and right == 1:
                return 1
            else:
                return 0
        elif op == '|':
            if left == 1 or right == 1:
                return 1
            else:
                return 0
        elif op == '<':
            if (left < right):
                return 1
            else:
                return 0
        elif op == '<=':
            if (left <= right):
                return 1
            else:
                return 0
        elif op == '>':
            if (left > right):
                return 1
            else:
                return 0
        elif op == '>=':
            if (left >= right):
                return 1
            else:
                return 0
        elif op == '=':
            if (left == right):
                return 1
            else:
                return 0
        elif op == '<>':
            if (left != right):
                return 1
            else:
                return 0
        else:
            raise SyntaxError("unknown operator %s" % op)

    @visitor(IfThenElse)
    def visit(self, ite):
        condition = ite.condition
        then_part = ite.then_part
        else_part = ite.else_part
        # as of now, else_part is compulsory
        if (condition):
            return then_part
        elif (else_part != None):
            return else_part
        else:
            return None
            

    @visitor(None)
    def visit(self, node):
        raise SyntaxError("no evaluation defined for %s" % node)
