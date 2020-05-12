'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é
divisível somente por ele mesmo e por 1.
'''
print('É seu primo?')
num = int(input('Digite um número:'))
tot = 0

for divisor in range(1, num + 1):
    if num % divisor == 0:
        print('\033[1;32m', end = ' ')
        tot += 1
    else:
        print('\033[1;34m', end=' ')
    print('{}'.format(divisor), end = '')

print('\nO número {} foi divisível por {} vezes.'.format(num, tot))

if tot == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')