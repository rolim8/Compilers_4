# Crie um programa que incrementa todos os números em uma frase.

def split(word):
    return [char for char in word]

lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

word = input('Digite uma frase: ').upper()
lst2 = split(word)

print(''.join([str(a) + b for a, b in zip(lst1, lst2)]))
