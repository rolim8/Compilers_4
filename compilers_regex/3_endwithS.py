# Crie um programa que insere a letra s no final das palavras que terminam com a letra O.

word = input("Palavra: ")

if word.endswith('O') or word.endswith('o'):
    print(f'{word}s')

else:
    print(f"\n{word} não termina em 'o'")