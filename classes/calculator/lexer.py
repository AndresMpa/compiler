import ply.lex as lex
import sys


tokens = (
    # Symbols
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'L_PARENT',
    'R_PARENT',

    # Others
    'ID',
    'NUMBER',
)

# Regular expressions rules for a simple tokens
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_L_PARENT = r'\('
t_R_PARENT = r'\)'

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

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
                fin = 'test.txt'
        f = open(fin, 'r')
        data = f.read()
        print (data)
        lexer.input(data)
        test(data, lexer)
