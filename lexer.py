import ply.lex as lex
import sys

# LISTA DE TOKENS
tokens = (
    # PALABRAS RESERVADAS
    '__HALT_COMPILER',
    'ABSTRACT',
    'AND',
    'ARRAY',
    'AS',
    'BREAK',
    'CALLABLE',
    'CASE',
    'CATCH',
    'CLASS',
    'CLONE',
    'CONST',
    'CONTINUE',
    'DECLARE',
    'DEFAULT',
    'DIE',
    'DO',
    'ECHO',
    'ELSE',
    'ELSEIF',
    'EMPTY',
    'ENDDECLARE',
    'ENDFOR',
    'ENDFOREACH',
    'ENDIF',
    'ENDSWITCH',
    'ENDWHILE',
    'EVAL',
    'EXIT',
    'EXTENDS',
    'FALSE',
    'FINAL',
    'FINALLY',
    'FN',  # Reemplaza function
    'FOR',
    'FOREACH',
    'FUNCTION',
    'GLOBAL',
    'GOTO',
    'IF',
    'IMPLEMENTS',
    'INCLUDE',
    'INCLUDE_ONCE',
    'INSTANCEOF'
    'INSTEADOF'
    'INTERFACE',
    'ISSET',
    'LIST',
    'MATCH',
    'NAMESPACE',
    'NEW',
    'OR',
    'PRINT',
    'PRIVATE',
    'PROTECTED',
    'PUBLIC',
    'REQUIRE',
    'RETURN',
    'STATIC',
    'SWITCH',
    'THROW',
    'TRAIT',
    'TRUE',
    'TRY',
    'UNSET',
    'USE',
    'VARIABLE',
    'WHILE',
    'XOR',
    'YIELD',

    # SIMBOLOS
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'MODULE',
    'EQUAL',
    'EQUALEQUAL',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'QUOTATIONMARKSD',
    'QUOTATIONMARKSS',
    'DOLLARSIGN',
    'ATSIGN',
    'DISTINT',
    'ORSYM',
    'XORSYM',
    'NOT',
    'QUESTIONMARK',


    # OTROS
    'ID',
    'VAR',
    'NUMBER',
    'STRING',
    'COMMENTS',
    'COMMENTS_SLASH',
    'COMMENTS_MULTILINE',
    'OPENPHP',
    'CLOSEPHP',
)

#######################
# EXPRESIONES REGULARES
#######################

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULE = r'\%'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_QUOTATIONMARKSD = r'\"'
t_QUOTATIONMARKSS = r'\''
t_DOLLARSIGN = r'\$'
t_ATSIGN = r'@'
t_DISTINT = r'!'

t_ORSYM = r'\|'
t_XORSYM = r'\^'
t_NOT = r'~'

t_QUESTIONMARK = r'\?'


#######################
# PALABRAS RESERVADAS
#######################


def t_HALT_COMPILER(t):
    r'__halt_compiler'
    return t


def t_ABSTRACT(t):
    r'abstract'
    return t


def t_AND(t):
    r'and'
    return t


def t_ARRAY(t):
    r'array'
    return t


def t_AS(t):
    r'as'
    return t


def t_BREAK(t):
    r'break'
    return t


def t_CALLABLE(t):
    r'callable'
    return t


def t_CASE(t):
    r'case'
    return t


def t_CATCH(t):
    r'catch'
    return t


def t_CLASS(t):
    r'class'
    return t


def t_CLONE(t):
    r'clone'
    return t


def t_CONST(t):
    r'const'
    return t


def t_CONTINUE(t):
    r'continue'
    return t


def t_DECLARE(t):
    r'declare'
    return t


def t_DEFAULT(t):
    r'default'
    return t


def t_DIE(t):
    r'die'
    return t


def t_DO(t):
    r'do'
    return t


def t_ECHO(t):
    r'echo'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_ELSEIF(t):
    r'elseif'
    return t


def t_EMPTY(t):
    r'empty'
    return t


def t_ENDDECLARE(t):
    r'enddeclare'
    return t


def t_ENDFOR(t):
    r'endfor'
    return t


def t_ENDFOREACH(t):
    r'endforeach'
    return t


def t_ENDIF(t):
    r'endif'
    return t


def t_ENDSWITCH(t):
    r'endswitch'
    return t


def t_ENDWHILE(t):
    r'endwhile'
    return t


def t_EVAL(t):
    r'eval'
    return t


def t_EXIT(t):
    r'exit'
    return t


def t_EXTENDS(t):
    r'extends'
    return t


def t_FALSE(t):
    r'false'
    return t


def t_FINAL(t):
    r'final'
    return t


def t_FINALLY(t):
    r'finally'
    return t


def t_FN(t):
    r'fn'
    return t


def t_FOR(t):
    r'for'
    return t


def t_FOREACH(t):
    r'foreach'
    return t


def t_FUNCTION(t):
    r'function'
    return t


def t_GLOBAL(t):
    r'global'
    return t


def t_GOTO(t):
    r'goto'
    return t


def t_IF(t):
    r'if'
    return t


def t_IMPLEMENTS(t):
    r'implements'
    return t


def t_INCLUDE(t):
    r'include'
    return t


def t_INCLUDEONCE(t):
    r'include_once'
    return t


def t_INSTANCEOF(t):
    r'instanceof'
    return t


def t_INSTEADOF(t):
    r'insteadof'
    return t


def t_INTERFACE(t):
    r'interface'
    return t


def t_ISSET(t):
    r'isset'
    return t


def t_LIST(t):
    r'list'
    return t


def t_MATCH(t):
    r'match'
    return t


def t_NAMESPACE(t):
    r'namespace'
    return t


def t_NEW(t):
    r'new'
    return t


def t_OR(t):
    r'or'
    return t


def t_PRINT(t):
    r'print'
    return t


def t_PRIVATE(t):
    r'private'
    return t


def t_PROTECTED(t):
    r'protected'
    return t


def t_PUBLIC(t):
    r'public'
    return t


def t_REQUIRE(t):
    r'require'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_STATIC(t):
    r'static'
    return t


def t_SWITCH(t):
    r'switch'
    return t


def t_THROW(t):
    r'throw'
    return t


def t_TRAIT(t):
    r'trait'
    return t


def t_TRUE(t):
    r'true'
    return t


def t_TRY(t):
    r'try'
    return t


def t_UNSET(t):
    r'unset'
    return t


def t_USE(t):
    r'use'
    return t


def t_VAR(t):
    r'var'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_XOR(t):
    r'xor'
    return t


def t_YIELD(t):
    r'yield'
    return t

#######################
# SIMBOLOS
#######################


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_MINUSMINUS(t):
    r'\-\-'
    return t


def t_EQUALEQUAL(t):
    r'=='
    return t


def t_LESSEQUAL(t):
    r'<='
    return t


def t_GREATEREQUAL(t):
    r'>='
    return t

#######################
# OTROS
#######################


def t_ESPECIAL_CASES(t):
    r'\d+[a-z|A-Z]+'
    print("Lexical error: " + str(t.value))


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_ID(t):
    r'[a-z|A-Z]+(_\d\w)*'
    return t


def t_VARIABLE(t):
    r'\$\w+(_\d\w)*'
    return t

# Cadena con comillas dobles o simples


def t_STRING(t):
    r'(\")(.)*(\")|(\')(.)*(\')'
    return t


def t_OPENPHP(t):
    r'<\?php'
    return t


def t_CLOSEPHP(t):
    r'\?>'
    return t


t_ignore = ' \t'

#Comentario de una linea con #


def t_COMMENTS(t):
    r'\#(.)*?\n'
    t.lexer.lineno += t.value.count('\n')

# Comentario de una linea con // el (.) es cualquier caracter menos newline


def t_COMMENTS_SLASH(t):
    r'\//(.)*?\n'
    t.lexer.lineno += t.value.count('\n')


# Comentarios de multiples lineas usando /* */

def t_COMMENTS_MULTILINE(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


def test(data, lexer):
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'test.php'
        f = open(fin, 'r')
        data = f.read()
        #print ("Read data: \n", data)
        lexer.input(data)
        test(data, lexer)
