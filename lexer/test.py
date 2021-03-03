from lexer import Lexer

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usando: lexer.py filename')
        sys.exit(1)

    code = open(sys.argv[1]).read()

    lx = Lexer()
    for token in lx.tokenize(code):
        print(token)
