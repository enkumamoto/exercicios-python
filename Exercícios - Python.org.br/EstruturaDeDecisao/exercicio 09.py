'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
print ('ih, desceu!')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

decrescente = [num1, num2, num3]

print (sorted(decrescente, reverse = True))
