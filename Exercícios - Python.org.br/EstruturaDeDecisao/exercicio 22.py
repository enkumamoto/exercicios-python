'''
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
'''
print ('É par ou ímpar?')

num1 = int(input('Digite um número inteiro: '))

if (num1 % 2) == 0:
    print(f'{num1} é par.')

else:
    print(f'{num1} é ímpar.')