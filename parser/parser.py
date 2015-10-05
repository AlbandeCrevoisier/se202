from ast.nodes import *
from . import tokenizer
import ply.yacc as yacc

tokens = tokenizer.tokens

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'INF', 'INFOREQ', 'SUP', 'SUPOREQ', 'EQ', 'DIFF'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV')
)


def p_expression_ifThenElse(p):
#    '''expression : IF expression THEN expression
#                  | IF expression THEN expression ELSE expression'''
#    p[0] = IfThenElse(p[1], p[3], p[5]=None)
    'expression : IF expression THEN expression ELSE expression'
    p[0] = IfThenElse(p[2], p[4], p[6])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression TIMES expression
                  | expression MINUS expression
                  | expression DIV expression
                  | expression INF expression
                  | expression INFOREQ expression
                  | expression SUP expression
                  | expression SUPOREQ expression
                  | expression EQ expression
                  | expression DIFF expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = BinaryOperator(p[2], p[1], p[3])

def p_expression_parentheses(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = IntegerLiteral(p[1])

def p_expression_identifier(p):
    'expression : ID'
    p[0] = Identifier(p[1])

#def p_let(p):
#    'expression : LET statement IN expression END'
#    p[0] = Let(

#def p_statement(p):
#    '''statement : decl_var_type
#                 | decl_var_notype
#                 | decl_fun'''
    

#def p_var_decl_type(p):
#    'var_decl_type : VAR ID COLON INT ASSIGN expression'
#    p[0] = VarDecl(Identifier(p[2]), Type(p[4]), p[6])

#def p_var_decl_notype(p):
#    'ar_decl_notype : VAR ID ASSIGN expression'
#    p[0] = VarDecl(Identifier(p[2]), Type('int'), p[4])

def p_error(p):
    import sys
    sys.stderr.write("no way to analyze %s\n" % p)
    sys.exit(1)

parser = yacc.yacc()

def parse(text):
    return parser.parse(text, lexer = tokenizer.lexer)

