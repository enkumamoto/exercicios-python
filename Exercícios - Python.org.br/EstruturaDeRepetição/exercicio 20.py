'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
fatorial a números inteiros positivos e menores que 16.
'''
import numpy
print('Fatorial')

num = int(input('Digite um número que gostaria de fatorar: '))
lista = []

while num <= 16:
    for item in range(num, 0, -1):
        lista.append(item)
        res = numpy.prod(lista)
        print(f'O fatorial de {num}! é:{res}')

    else:
        break