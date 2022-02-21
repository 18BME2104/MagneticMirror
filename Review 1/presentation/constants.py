    class Constants:
        def __init__(self):
            self.constants = { 
                #'symbol': ['value', unit', 'digits', '10 ^ power', 'number of digits', 'description'],
                 }
        def show_constant(self, symbol):
            if symbol in constants.keys():
                (print(f'{symbol} = {constants[symbol][1]} x 10^({constants[symbol][2]}) {constants[symbol][0]} \
                 \n {constants[symbol][3]} significant figures \
                 \n {constants[symbol][4]}'))
            else:
                print('Constant not in record or symbol mismatch.')
