'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
n−ésimo termo.
'''
print('Fibonaaaaaaaaaaaaaaaaaaaaaaaaaacci!')
n = int(input('Digite a posição do termo que quer encontrar: '))

ultimo = 1
penultimo = 1

if n == 1 or n == 2:
    print ('1')
else:
    count = 3
    while count <= n:
        termo = ultimo + penultimo
        # print(f'A soma de {ultimo} com {penultimo} gera o termo {termo}')
        penultimo = ultimo
        ultimo = termo
        count += 1

    print (f'O termo na posição {n} da sequência de Fibonacci é {termo}.')