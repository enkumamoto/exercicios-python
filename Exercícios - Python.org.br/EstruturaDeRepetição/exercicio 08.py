'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
print('Digite 5 números e informo o a soma e a média')

numeros = int(input('Quantos números quer somar e tirar média? '))
num = int(input('Digite um número: '))
count = 1
maior = num
soma = num

while count < numeros:
    count += 1
    temp = int(input('Digite o %d número : '%count))
    soma += temp
    if temp > maior:
        maior = temp

media = soma /numeros
print(f'A soma dos números é {soma}')
print(f'A média da soma dos números é: {media}')

