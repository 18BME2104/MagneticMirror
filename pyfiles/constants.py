import numpy as np # For computations
import sympy as sm # For symbolic use

import pandas as pd # To use large tables
import matplotlib.pyplot as plt #To make plots

constants = { 
            #'symbol': ['unit', 'value', '10 ^ power', 'number of digits', 'description'],
            'e' : ['C', 1.602176634, -19, 10, 'The charge of an electron, or the elementary charge'],
            'm_e': ['kg', 9.109383701, -31, 10, 'The mass of an electron'],
            'amu': ['kg', 1.6605390666, -27, 11, 'The unified atomic mass unit or Dalton'],
            'N_A': ['mol', 6.02214076, 23, 9, 'Avogadro\'s number']
                    }
def show_constant(symbol):
    if symbol in constants.keys():
        (print(f'{symbol} = {constants[symbol][1]} x 10^({constants[symbol][2]}) {constants[symbol][0]} \
               \n {constants[symbol][3]} significant figures \
               \n {constants[symbol][4]}'))
    else:
        print('Constant not in record or symbol mismatch.')
