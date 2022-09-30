import ply.yacc as yacc
from lexer import tokens
import lexer
import sys

VERBOSE = 1

def p_basic(p):
    '''
    basic : basic PLUS operation
            | basic MINUS operation
            | operation
    '''
    pass

def p_operation(p):
    '''
    operation : operation TIMES declaration 
            | operation DIVIDE declaration 
            | declaration
    '''
    pass

def p_declaration(p):
    '''
    declaration : L_PARENT basic R_PARENT
            | ID
            | NUMBER
    '''
    pass

def p_error(p):
    if VERBOSE:
        if p is not None:
            print("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) +
                  " NO SE ESPERABA EL TOKEN  " + str(p.value))
        else:
            print("ERROR SINTACTICO EN LA LINEA: " + str(p.lexer.lineno))
    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        file = sys.argv[1]
    else:
        file = 'test.txt'

    file_data = open(file, 'r')
    data = file_data.read()
    #print (data)
    parser.parse(data, tracking=True)
    print("Archivo reconocido satisfactoriamente por el parser")
    # input()
