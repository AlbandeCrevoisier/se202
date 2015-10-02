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
        left = binop.left.accept(self)
        op = binop.op
        # short-circuit
        if op == '&':
            if left != 0:
                right = binop.right.accept(self)
                if right != 0:
                    return 1
            return 0
        elif op == '|':
            if left != 0:
                return 1
            else:
                right = binop.right.accept(self)
                if right != 0:
                   return 1
            return 0

        # non short-circuit operators
        right = binop.right.accept(self)
        if op == '+':
            return left + right
        elif op == '*':
            return left * right
        elif op == '-':
            return left - right 
        elif op == '/':
            return left // right 
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
        condition = ite.condition.accept(self)
        then_part = ite.then_part.accept(self)
        else_part = ite.else_part.accept(self)
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
