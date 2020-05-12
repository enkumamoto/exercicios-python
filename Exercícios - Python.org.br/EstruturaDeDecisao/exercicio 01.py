'''
Faça um Programa que peça dois números e imprima o maior deles. 
'''
print ('Quem é o maior?')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 == num2:
    print('Você digitou o mesmo número... Tenta novamente')

elif num1 > num2:
    print(f'Entre os números escolhidos, {num1} é o maior!')

else:
    print(f'Entre os números escolhidos, {num2} é o maior!')
