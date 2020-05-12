'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
print ('Quem é o que?')

count = 0
pares = 0
impares = 0

while count < 10:
    count += 1
    num = int(input('Digite um número: '))
    if (num % 2) == 0:
        num = pares
        pares += 1

    else:
        num = impares
        impares += 1

print(f'{impares} números ímpares e {pares} números pares.')