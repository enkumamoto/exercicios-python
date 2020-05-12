'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
'''
print('O Programa precisa de 2 números inteiros e um número real.\nPara que o Calculo mostre:\no produto do dobro do primeiro com metade do segundo .\na soma do triplo do primeiro com o terceiro.\no terceiro elevado ao cubo.')
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um numero real, por exemplo ('-1', '4.2345', '-0.3': "))
print(' ')

res1 = ((num1 * 2) * (num2 / num2))
res2 = ((num1 * 3)) + num3
res3 = num3 ** 3
print(' ')

print(f'O produto do dobro o primeiro com metade do segundo é {res1}.')
print(f'A soma do triplo do primeiro com o terceiro é {res2}.')
print(f'O terceiro elevado ao cubo é {res3}.')
