'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''
soma = 0
numero = []
lista_num = []

print ('Para parar o programa digite 0')
num = int(input('Digite o número: '))
while num != 0:
    num = int(input('Digite o número: '))
    soma += num
    numero.append(num)
    while num > 1000 or num < 0:
        lista_num.append(num)
        print('O número deve ser maior que 0 e menor que 1000.')
        num = int(input('Digite o número: '))

print(numero)
# print(f'A soma dos número é: {soma}')
# print('O maior número é:', max(numero))
# print('O menor número é:', min(numero))