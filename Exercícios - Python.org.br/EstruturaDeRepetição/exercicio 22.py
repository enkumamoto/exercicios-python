'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
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


if tot == 2:
    print(f'É um número primo!')
else:
    print('\nO número {} foi divisível por {} vezes.'.format(num, tot))
    print(f'Não é um número primo!')