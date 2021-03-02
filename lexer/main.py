from lexer import Lexer as lx

def main():
    code = ''
    lexer = lx()
    while code != 'exit()':
        code = input("> ")
        if code != "exit()":
            # clearCode(code)
            try:
                for token in lexer.tokenize(code):
                    print(token)
            except EOFError:
                break
        else:
            break

main()
