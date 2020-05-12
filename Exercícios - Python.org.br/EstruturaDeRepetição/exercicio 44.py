'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

    1 , 2, 3, 4  - Votos para os respectivos candidatos
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco

Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos.

Para finalizar o conjunto de votos tem-se o valor zero.
'''

print('Eleições da Marmelada')
print('Bem vinda(o) a Urna Eletrônica')
print('Vote em um dos candidatos a presidência:\n1 - Ananda Seabra Kumamoto\n2 - Maria Eduarda\n3 - Ana Carolina\n4 - Júnior')
print('Para votar Nulo, digite 5.\nPara votar em branco, digite 6.')
print('Para encerrar a votação, digite 0.')

votos = []

while True:
    urna = int(input('Digite o seu voto: '))
    if urna == 0:
        break
    while urna > 6 or urna < 0:
        print('Opção Inválida.\nUse uma das opções da lista.')
        urna = int(input('Digite o seu voto: '))

    votos.append(urna)

prct_nulo = float(((votos.count(5) * 100) / len(votos)))
prct_branco = float(((votos.count(6) * 100) / len(votos)))

print('Total de votos:',len(votos))
print('Total de votos para Ananda Seabra Kumamoto:',votos.count(1))
print('Total de votos para Maria Eduarda:',votos.count(2))
print('Total de votos para Ana Carolina:',votos.count(3))
print('Total de votos para Júnior:',votos.count(4))
print('Total de votos nulos:',votos.count(5))
print('Total de votos brancos:',votos.count(6))
print(f'O percentual de votos nulos sobre total de votos é de: %.1f'%prct_nulo)
print(f'O percentual de votos brancos sobre total de votos é de: %.1f'%prct_branco)
