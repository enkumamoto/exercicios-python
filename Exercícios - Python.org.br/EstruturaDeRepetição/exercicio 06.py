'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele
mostre os números um ao lado do outro.
'''
x = 0  # colunas
while x < 21:
    print(x)
    x += 1
print ('Fim!')
print('---')

x = 0  # colunas
while x < 21:
    y = 0  # linhas

    while y < 21:
        print (f'{x} {y}')
        y+= 1
    x += 1
print ('Fim!')
print('---')