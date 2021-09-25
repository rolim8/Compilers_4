# Crie uma expressão regular que verifique se uma frase contém uma quantidade ímpar de letras a.

string = input("Digite uma frase: ")

count = 0

for i in string:
    if i == 'a'|i == 'á'|i == 'â':
        count += 1

if count % 2 == 1:
    print(f"\nContagem de letras A em {string} é {str(count)} que é IMPAR")

else:
    print(f"\nContagem de letras A em {string} é {str(count)} que é PAR")
