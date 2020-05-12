'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve
ser conforme o exemplo abaixo:

    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
'''
print('Fatorial')

num = int(input('Digite um número que gostaria de fatorar: '))
c = num
f = 1

print('Fatorando de: {}\n{}! = '.format(num,num),end = '')

while c > 0:
    print('{}'.format(c), end = '')
    print(' . ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1

print('{}'.format(f))