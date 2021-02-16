# Basic language
import basic
# This var will catch the code I write
code = ''

while code != 'exit':
    code = input('> ')
    if code != 'exit'
        # This is catching error an the compilator exiting code
        result, error = basic.run('example.apa', code)

        # If there's a error this line show it, else it shows exiting code
        if error:
            print(error.as_string())
        else:
            print(result)
