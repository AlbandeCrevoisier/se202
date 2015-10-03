import unittest

from ast.evaluator import Evaluator
from ast.nodes import IntegerLiteral, BinaryOperator, IfThenElse, BinaryOperator
from parser.parser import parse

class TestEvaluator(unittest.TestCase):

    def check(self, ast, expected):
        self.assertEqual(ast.accept(Evaluator()), expected)

    def parse_check(self, str, expected):
        self.assertEqual(parse(str).accept(Evaluator()), expected)

    def test_literal(self):
        self.check(IntegerLiteral(42), 42)

    def test_basic_operator(self):
        self.check(BinaryOperator('+', IntegerLiteral(10), IntegerLiteral(20)), 30)

    def test_binop(self):
        self.check(BinaryOperator('*', IntegerLiteral(6), IntegerLiteral(7)), 42)
        self.check(BinaryOperator('-', IntegerLiteral(10), IntegerLiteral(1)), 9)
        self.check(BinaryOperator('/', IntegerLiteral(42), IntegerLiteral(7)), 6)
        self.check(BinaryOperator('/', IntegerLiteral(42), IntegerLiteral(5)), 8)
        self.check(BinaryOperator('&', IntegerLiteral(0), IntegerLiteral(0)), 0)
        self.check(BinaryOperator('&', IntegerLiteral(0), IntegerLiteral(1)), 0)
        self.check(BinaryOperator('&', IntegerLiteral(1), IntegerLiteral(0)), 0)
        self.check(BinaryOperator('&', IntegerLiteral(1), IntegerLiteral(1)), 1)
        self.check(BinaryOperator('|', IntegerLiteral(0), IntegerLiteral(0)), 0)
        self.check(BinaryOperator('|', IntegerLiteral(0), IntegerLiteral(1)), 1)
        self.check(BinaryOperator('|', IntegerLiteral(1), IntegerLiteral(0)), 1)
        self.check(BinaryOperator('|', IntegerLiteral(1), IntegerLiteral(1)), 1)
        self.check(BinaryOperator('<', IntegerLiteral(0), IntegerLiteral(1)), 1)
        self.check(BinaryOperator('<', IntegerLiteral(1), IntegerLiteral(1)), 0)
        self.check(BinaryOperator('<', IntegerLiteral(1), IntegerLiteral(0)), 0)
        self.check(BinaryOperator('<=', IntegerLiteral(0), IntegerLiteral(1)), 1)
        self.check(BinaryOperator('<=', IntegerLiteral(1), IntegerLiteral(1)), 1)
        self.check(BinaryOperator('<=', IntegerLiteral(1), IntegerLiteral(0)), 0)
        self.check(BinaryOperator('>', IntegerLiteral(0), IntegerLiteral(1)), 0)
        self.check(BinaryOperator('>', IntegerLiteral(1), IntegerLiteral(1)), 0)
        self.check(BinaryOperator('>', IntegerLiteral(1), IntegerLiteral(0)), 1)
        self.check(BinaryOperator('>=', IntegerLiteral(0), IntegerLiteral(1)), 0)
        self.check(BinaryOperator('>=', IntegerLiteral(1), IntegerLiteral(1)), 1)
        self.check(BinaryOperator('>=', IntegerLiteral(1), IntegerLiteral(0)), 1)
        self.check(BinaryOperator('=', IntegerLiteral(0), IntegerLiteral(1)), 0)
        self.check(BinaryOperator('=', IntegerLiteral(1), IntegerLiteral(1)), 1)
        self.check(BinaryOperator('<>', IntegerLiteral(0), IntegerLiteral(1)), 1)
        self.check(BinaryOperator('<>', IntegerLiteral(1), IntegerLiteral(1)), 0)

    def test_ifThenElse(self):
        self.check(IfThenElse(IntegerLiteral(42), IntegerLiteral(2), IntegerLiteral(3)), 2)
        self.check(IfThenElse(IntegerLiteral(0), IntegerLiteral(2), IntegerLiteral(3)), 3)

    def test_priorities(self):
        self.check(BinaryOperator('+', IntegerLiteral(1), BinaryOperator('*', IntegerLiteral(2), IntegerLiteral(3))), 7)

    def test_parse_literal(self):
        self.parse_check('42', 42)

    def test_parse_sequence(self):
        self.parse_check('1+(2+3)+4', 10)

    def test_precedence(self):
        self.parse_check('1 + 2 * 3', 7)
        self.parse_check('2 * 3 + 1', 7)
        
    def test_precedence_(self):
        self.parse_check('1 + 2 - 3', 0)
        self.parse_check('2 - 3 + 1', 0)
        self.parse_check('1 + 2 / 3', 1)
        self.parse_check('2 / 3 + 1', 1)
        self.parse_check('3 - 2 * 1', 1)
        self.parse_check('3 * 2 - 1', 5)
        self.parse_check('1 - 2 / 3', 1)
        self.parse_check('3 / 2 - 1', 0)
        self.parse_check('0 = 0 = 0', 0)
        self.parse_check('1 | 2 / 0', 1) # short-circuit
        self.parse_check('0 & 2 / 0', 0)
        self.parse_check('1 & 1 | 0 & 0', 1)


if __name__ == '__main__':
    unittest.main()
