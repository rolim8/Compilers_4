#Crie uma expressão regular que verifique se uma estrutura de parênteses está correta.

import re

open_list = ["("]
close_list = [")"]


def check(str):
    stack = []

    for i in str:

        if i in open_list:
            stack.append(i)

        elif i in close_list:
            pos = close_list.index(i)

            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()

            else:
                return "DESBALANCEADO"

    if len(stack) == 0:
        return "BALANCEADO"

    else:
        return "DESBALANCEADO"


string = "()(hello)"
print(string, "-", check(string))

