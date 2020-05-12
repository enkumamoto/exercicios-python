'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o
funcionamento, o estilo e o número de testes (divisões) executados.
'''
print('É seu primo?')

num = int(input('Digite um número:'))
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

print('\n\033O número {} foi divisível por {} vezes.'.format(num, tot))

if tot == 2:
    print(f'{div} é um número primo!')
else:
    print('Não é um número primo!')
