# Crie um programa utilizando expressões regulares que inverta a ordem do seguinte texto:

import re


def check(str):
    return re.sub(r'(\w+)\:\s(\w+)', r'\g<2>: \g<1>', str)


print(check("Key1: 11224 \nKey2: 524 \nKey3: 5125 \nAbc: 51252"))