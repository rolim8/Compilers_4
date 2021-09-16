# Crie uma expressão regular que reconhece números decimais.

import re

regexNum = '^[0-9]+$'


def check(str):
    if re.search(regexNum, str):
        print(f"'{str}' É NÚMERO")
    else:
        print(f"'{str}' NÃO É NÚMERO")


if __name__ == '__main__':

    str = input("Digite um valor: ")
    check(str)
