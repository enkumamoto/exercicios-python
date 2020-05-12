'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.
'''
print ('Mostrador de notas sem futuro')

while True:
    nota = float(input('Digite uma nota entre 0 e 10: '))

    if nota >= 0 and nota <= 10:
        print (f'O valor da nota é {nota}')
        break
    else:
        print (f'O valor {nota} é inválido, digite uma nota válida')


