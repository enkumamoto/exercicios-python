'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
print ('Teje preso! ou num teje?')
print('\n')
print('Gostaria de fazer algumas perguntas.\nPor favor responda com Sim ou Não:')

tel = input("Telefonou para a vítima? ").lower()
local = input("Esteve no local do crime? ").lower()
mora = input("Mora perto da vítima? ").lower()
devia = input("Devia para a vítima? ").lower()
trabalhou = input("Já trabalhou com a vítima? ").lower()

sim = 0
nao = 0

if tel and local and mora and devia and trabalhou == 'sim':
    sim = sim + 1

elif tel and local and mora and devia and trabalhou == 'nao':
    nao = nao + 1

else:
    print ('Dados inválidos')

if sim == 5:
    print ('Assassino')

elif sim < 5 and sim > 2:
    print ('Cúmplice')

elif sim <= 2 and sim > 0:
    print ('Suspeito')

else:
    print ('Inocente')