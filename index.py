import sys

import interpreter
import parser
import lexer

if len(sys.argv) == 2:
    with open(sys.argv[1]) as file:
        data = file.read()

    intructions = parser.parse(data)

    if not intructions:
        raise SystemExit

    basicInterpreter = interpreter.BasicInterpreter(intructions)

    try:
        basicInterpreter.run()
        raise SystemExit
    except RuntimeError:
        pass

else:
    print("""
    Welcome!

    This is an implementation of Dartmouth BASIC (1964), version 1.0.0
    Type "help" from more information, to exit ctrl + c
    """)
    basicInterpreter = interpreter.BasicInterpreter({})

# Command Line Interpreter

# This works like python, node, bash, etc interactive interpreters
# it also supports reading entire files by passing them trough command
# see the previous mode
while True:
    # To handle text inputs
    try:
        line = input("> ")
    except EOFError:
        raise SystemExit
    except KeyboardInterrupt:
        print("Goodbye!")
        exit(1)

    if not line:
        continue
    
    line += "\n"

    sentence = parser.parse(line)

    if not sentence:
        continue
