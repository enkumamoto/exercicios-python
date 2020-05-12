'''
Altere o programa anterior para mostrar no final a soma dos números.
'''
print('De onda até aonde?')
onde = int(input('Digite um numéro inteiro para o inicio da contagem: '))
aonde = int(input('Digite um numéro inteiro para o final da contagem: '))

for n in range(onde, (aonde +1)):
    print(n)
    soma = onde + aonde
print(f'A soma de {onde} e {aonde} é igual a: {soma}')