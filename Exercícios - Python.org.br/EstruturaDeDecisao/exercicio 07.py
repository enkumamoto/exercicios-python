'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
print ('Quem é o maior e o menor?')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

maior = num1
menor = num1

if maior < num2:
    maior = num2

elif maior < num3:
    maior = num3

elif menor > num2:
    menor = num2

elif menor > num3:
    menor = num3

else:
    print ('Algo deu errado, tente novamente.')

print(f'Entre os números escolhidos, {maior} é o maior e o {menor} é o menor!')