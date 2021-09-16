# Crie uma expressão regular que reconhece tags html.

import re


def check(str):
    regex = (#"((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    p = re.compile(regex)

    if (str == None):
        return False

    if (re.search(p, str)):
        return True
    else:
        return False


url = input('INFORME UMA URL: ')

if check(url):
    print(f"{url} \n --> É UM ENDEREÇO URL VÁLIDO")

else:
    print(f"{url} \n --> 'NÃO' É UM ENDEREÇO URL VÁLIDO")