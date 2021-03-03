from lexer import Lexer as lx

def main():
    code = ''
    lexer = lx()
    while code != 'exit()':
        code = input("> ")
        if code != "exit()":
            try:
                # \d+[a-zA-Z]+ 888ggg
                # \d+.\d+ 8.8.8          
                for token in lexer.tokenize(code):
                    print(token)
            except EOFError:
                break
        else:
            break

main()
