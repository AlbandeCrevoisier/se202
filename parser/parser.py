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

def p_expression_ifThenElse(p):
#    '''expression : IF expression THEN expression
#                  | IF expression THEN expression ELSE expression'''
#    p[0] = IfThenElse(p[1], p[3], p[5]=None)
    'expression : IF expression THEN expression ELSE expression'
    p[0] = IfThenElse(p[2], p[4], p[6])


def p_let(p):
    'expression : LET decls IN expression END'
    p[0] = Let(p[2], p[4])

def p_decls(p):
    '''decls : decl
             | decls decl'''
    if (len(p) == 1):
        p[0] = p[1]
    else:
        p[0] = p[1], p[2]


def p_decl(p):
    '''decl : vardecl
            | fundecl'''
    

def p_var_decl_type(p):
    'vardecl : VAR ID COLON INT ASSIGN expression'
    p[0] = VarDecl(Identifier(p[2]), Type(p[4]), p[6])

def p_var_decl_notype(p):
    'vardecl : VAR ID ASSIGN expression'
    p[0] = VarDecl(Identifier(p[2]), Type(None), p[4])

def p_error(p):
    import sys
    sys.stderr.write("no way to analyze %s\n" % p)
    sys.exit(1)

parser = yacc.yacc()

def parse(text):
    return parser.parse(text, lexer = tokenizer.lexer)

