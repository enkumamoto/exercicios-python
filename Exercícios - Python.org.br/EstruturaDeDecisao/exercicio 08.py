'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.
'''
print ('Só sai barato.')


preco1 = int(input('Digite o preço do primeiro produto: R$ '))
preco2 = int(input('Digite o preço do segundo produto: R$ '))
preco3 = int(input('Digite o preço do terceiro produto: R$ '))


menor = preco1

if menor > preco2:
    menor = preco2
    print ('Leve o segundo produto!')

elif menor > preco3:
    menor = preco3
    print ('Leve o terceiro produto!')

else:
    print ('Leve o primeiro produto!')
