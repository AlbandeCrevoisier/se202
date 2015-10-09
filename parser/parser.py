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
    'expression : LET decls IN expressions END'
    p[0] = Let(p[2], [p[4]])

def p_decls(p):
    '''decls : decl
             | decls decl'''
    if (len(p) == 2):
        p[0] = [p[1]]
    else:
        p[0] = p[1] + p[2]

def p_decl(p):
    '''decl : vardecl
            | fundecl'''
    p[0] = p[1]

def p_vardecl(p):
    '''vardecl : VAR ID COLON INT ASSIGN expression
               | VAR ID ASSIGN expression'''
    if (len(p) == 7):
        p[0] = VarDecl(Identifier(p[2]), Type(p[4]), p[6])
    else:
        p[0] = VarDecl(Identifier(p[2]), None, p[4])

def p_params(p):
    '''params :
                | param
                | params COMMA param'''
    if (len(p) == 1):
        p[0] = []
    elif (len(p) == 2):
        p[0] = [p[1]]
    else:
        p[0] = p[1] + p[2]

def p_param(p):
    'param : ID COLON INT'
    p[0] = VarDecl(Identifier(p[1]), Type(p[3]), None)

def p_fundecl(p):
    '''fundecl : FUNCTION ID LPAREN params RPAREN COLON INT EQ expression
               | FUNCTION ID LPAREN params RPAREN EQ expression'''
    if (len(p) == 10):
        p[0] = FunDecl(Identifier(p[3]), p[5], Type(p[7]), p[8])
    else:
        p[0] = FunDecl(Identifier(p[3]), p[5], None, p[7])

def p_expressions(p):
    '''expressions : expression
                   | expressions SEMICOLON expression'''
    if (len(p) == 2):
        p[0] = [p[1]]
    else:
        p[0] = p[1] + p[2]

def p_error(p):
    import sys
    sys.stderr.write("no way to analyze %s\n" % p)
    sys.exit(1)

parser = yacc.yacc()

def parse(text):
    return parser.parse(text, lexer = tokenizer.lexer.clone())
