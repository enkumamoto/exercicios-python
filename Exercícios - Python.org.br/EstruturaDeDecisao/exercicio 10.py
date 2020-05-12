'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

print ("Qual o seu turno?")

turno = input("Qual dos turnos abaixo você estuda?\n1 - Digite M para Matutino\n2 - Digite V para Vespertino\n3 - N para Noturno\n\nDigite uma das opções: ").lower()

if turno == 'm':
    print('Bom Dia!')

elif turno == 'v':
    print('Boa Tarde!')

elif turno == 'n':
    print('Boa Noite!')

else:
    print("Valor Inválido!")