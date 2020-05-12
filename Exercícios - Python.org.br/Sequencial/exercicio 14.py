'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

print ('Calculo do excesso da cota de peixes')

pescador = input('Digite o nome do pescador: ')
pescado = float(input('Digite o peso total do que foi pescado em KG: '))
excesso = pescado - 50
multakg = excesso * 4

if pescado > 50:
    print(f'Prezado {pescador}\nVerificamos a carga do seu barco\ne a mesma tem um total de {pescado}kg.\nInfelizmente, por este excesso de {excesso}kg.\nEntão será cobrada uma multa no valor de R${multakg}.')

else:
    print (f'Prezado {pescador}, sua carga não excedeu os limites, com isso não há multa.')