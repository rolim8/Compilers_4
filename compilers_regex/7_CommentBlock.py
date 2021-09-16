# Crie uma expressão regular que reconheça comentários de bloco (/* */)

import re


def check(str):
    return [
        m.group(1)

        for m in re.finditer(
            r".*/\*(.+)\*/.*",
            str
        )
    ]


print(check("/*HELLO WORLD, THAT'S ALL*/"))