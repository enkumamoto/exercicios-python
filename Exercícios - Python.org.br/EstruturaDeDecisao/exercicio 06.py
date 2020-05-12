'''
Faça um Programa que leia três números e mostre o maior deles.
'''
print ('Quem é o maior?')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

if num1 == num2 or num1 == num3:
    print('Você digitou o mesmo número... Tenta novamente')

elif num1 > num2 and num1 > num3:
    print(f'Entre os números escolhidos, {num1} é o maior!')

elif num2 > num1 and num2 > num3:
    print(f'Entre os números escolhidos, {num2} é o maior!')
else:
    print(f'Entre os números escolhidos, {num3} é o maior!')