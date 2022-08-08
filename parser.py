from ply import *

parser = yacc.yacc()

def parse(data, debug=0):
    parser.error = 0
    parsed_sentence = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return parsed_sentence
