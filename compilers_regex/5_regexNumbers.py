# Crie uma expressão regular que reconhece números decimais.

import re

regexNum = r'^\d*[.,]?\d*$'


def check(str):
    if re.search(regexNum, str):
        print(f"'{str}' É UM NÚMERO VÁLIDO")
    else:
        print(f"'{str}' NÃO É UM VALOR VÁLIDO")


if __name__ == '__main__':

    str = input("Digite um valor: ")
    check(str)
