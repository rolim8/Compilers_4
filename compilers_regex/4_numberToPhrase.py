# Crie um programa que incrementa todos os números em uma frase.

import re

word = input('Digite uma frase: ').upper()

num_list = re.findall(r'\d+', word)
num_list = list(map(lambda x: int(x) + 1, num_list))

sent_list = re.split(r'\d+', word)
print(sent_list)
sent = ''

for sentence in sent_list:
    sent += sentence
    if len(num_list)>0:
        sent += str(num_list.pop(0))

print(sent)
