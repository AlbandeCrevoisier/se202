import ply.lex as lex

# Declare states.
states = (
    ('ccomment', 'exclusive'),
    )

# List of keywords. Each keyword will be returned as a token of a specific
# type, which makes it easier to match it in grammatical rules.
keywords = {'array': 'ARRAY',
            'break': 'BREAK',
            'do': 'DO',
            'else': 'ELSE',
            'end': 'END',
            'for': 'FOR',
            'function': 'FUNCTION',
            'if': 'IF',
            'in': 'IN',
            'int': 'INT',
            'let': 'LET',
            'nil': 'NIL',
            'of': 'OF',
            'then': 'THEN',
            'to': 'TO',
            'type': 'TYPE',
            'var': 'VAR',
            'while': 'WHILE'}

# List of tokens that can be recognized and are handled by the current
# grammar rules.
tokens = ('PLUS', 'TIMES', 'MINUS', 'DIV',
          'INF', 'INFOREQ', 'SUP', 'SUPOREQ', 'EQ', 'DIFF',
          'AND', 'OR',
          'COMMA', 'SEMICOLON',
          'LPAREN', 'RPAREN',
          'NUMBER', 'ID',
          'COLON', 'ASSIGN') \
          + ('IF', 'THEN', 'ELSE') \
          + ('LET', 'IN', 'END') \
          + ('FUNCTION', 'VAR', 'INT') \
          + ('WHILE', 'DO', 'FOR', 'TO', 'BREAK')

t_PLUS = r'\+'
t_MINUS = r'\-' 
t_TIMES = r'\*'
t_DIV = r'\/'
t_EQ = r'\='
t_DIFF = r'\<\>'
t_SUP = r'\>'
t_INF = r'\<'
t_SUPOREQ = r'\>\='
t_INFOREQ = r'\<\='
t_AND = r'\&'
t_OR = r'\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_ASSIGN = r':='
t_COMMA = r','
t_SEMICOLON = r';'

t_ignore = ' \t'

# Count lines when newlines are encountered
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Distinguish between identifier and keyword. If the keyword is not also
# in the tokens list, this is a syntax error pure and simple since we do
# not know what to do about it.
def t_ID(t):
    r'[A-Za-z][A-Za-z\d_]*'
    if t.value in keywords:
        t.type = keywords.get(t.value)
        if t.type not in tokens:
            raise lex.LexError("unhandled keyword %s" % t.value, t.type)
    return t

# Recognize number - no leading 0 are allowed
def t_NUMBER(t):
    r'[1-9]\d*|0'
    t.value = int(t.value)
    return t

# Single line comments
def t_SLCOMMENT(t):
    r'\/\/.*'
    pass

# Enter C comment
def t_ANY_begin_ccomment(t):
    r'\/\*'
    t.lexer.push_state('ccomment')

# Exit C comment
def t_ccomment_end(t):
    r'\*\/'
    t.lexer.pop_state()

# Discard non "/*" or "*/"
def t_ccomment_CCOMMENT(t):
    r'(\/ | \*)+'
    pass

t_ccomment_ignore_DISCARD = r'[^*/]'
t_ccomment_ignore = ''

def t_ANY_error(t):
    raise lex.LexError("unknown token %s" % t.value, t.value)

lexer = lex.lex()
