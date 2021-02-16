import basic
input_code = ''

while input_code != 'exit':
    input_code = input('> ')
    if input_code != 'exit':
        result, error = basic.run('example.dre', input_code)

        if error: print(error.as_string())
        else: print(result)
