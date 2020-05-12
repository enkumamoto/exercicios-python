'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
print ('Negativo ou Positivo?')
num1 = int(input('Digite um número Positivo ou Negativo: '))

if num1 == 0:
    print('Oh, ¬¬ o zero não vale...')

elif num1 > 0:
    print(f'O {num1} é positivo! :)')

else:
    print(f'O {num1} é negativo! :)')