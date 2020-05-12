'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
'''
print('números demais, arredonda!')

num1 = float(input("Digite qualquer número (Ex.: 123.456): "))

if num1 == round(num1):
    print('Inteiro')
else:
    print('Decimal')
    print('Arredondando para baixo:',round(num1 - 0.5))
    print('Arredondando para cima:',round(num1 + 0.5))