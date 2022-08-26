import ply.lex as lex
import sys

# lista de tokens
tokens = (
    # Reserverd words
    'AUTO',
    'ELSE',
    'BREAK', 
    'CASE',
    'IF',
    'INT',
    'LONG',
    'SHORT',
    'DOUBLE',
    'FLOAT',
    'CHAR',
    'BOOLEAN',
    'DEFINE',
    'INCLUDE',
    'DEFAULT', 
    'FOR',
    'SWITCH',
    'RETURN',
    'VOID',
    'WHILE',
   
    # Symbols
    'PLUS',
    'PLUSPLUS',
    #'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    #'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',

    # Others   
    'ID', 
    'NUMBER',
)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'

def t_AUTO(t):
    r'auto'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_INCLUDE(t):
    r'include'
    return t


def t_DEFINE(t):
    r'define'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DO(t):
    r'do'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IF(t):
    r'if'
    return t

def t_INT(t):
	r'int'
	return t

def t_SHORT(t):
    r'short'
    return t

def t_LONG(t):
    r'long'
    return t

def t_RETURN(t):
	r'return'
	return t

def t_SWITCH(t):
        r'switch'
        return t

def t_VOID(t):
	r'void'
	return t
	
def t_WHILE(t):
	r'while'
	return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion.c'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	#input()

