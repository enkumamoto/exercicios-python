'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''
soma = 0
numero = []

print ('Para parar o programa digite 0')

while True:
    num = int(input('Digite o número: '))
    if num != 0:
        soma += num
        numero.append(num)

    else:
        break

print(f'A soma dos número é: {soma}')
print('O maior número é:', max(numero))
print('O menor número é:', min(numero))
