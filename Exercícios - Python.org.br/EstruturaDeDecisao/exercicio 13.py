'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
outro valor deve aparecer valor inválido.
'''
def semana ():
    if dia == 1:
        return 'Domingo'

    elif dia == 2:
        return 'Segunda'

    elif dia == 3:
        return 'Terça'

    elif dia == 4:
        return 'Quarta'

    elif dia == 5:
        return 'Quinta'

    elif dia == 6:
        return 'Sexta'

    elif dia == 7:
        return 'Sábado'

    else:
        return 'Valor Inválido'

print ('Qual é o dia?')

dia = int(input('Digite de 1 a 7 para saber o dia da semana: '))
print (semana())