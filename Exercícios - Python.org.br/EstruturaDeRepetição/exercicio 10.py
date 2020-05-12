'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''
print('De onda até aonde?')
onde = int(input('Digite um numéro inteiro para o inicio da contagem: '))
aonde = int(input('Digite um numéro inteiro para o final da contagem: '))

for n in range(onde, (aonde +1)):
    print(n)
