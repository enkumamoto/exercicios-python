'''
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1
e um número inteiro informado pelo usuário.
'''
print('É seu primo sem limites?')
num = int(input('Digite um número para ser o limite para gerar números primos:'))
tot = 0
div = []

for divisor in range(1, num + 1):
    if num % divisor == 0:
        print('\033[1;32m', end = ' ')
        div.append(divisor)
        tot += 1
    else:
        print('\033[1;34m', end=' ')
    print('{}'.format(divisor), end = '')

if tot == 2:
    print(f'\nOs números primos são: {div}')
else:
    print(f'\n{num} não é primo.')