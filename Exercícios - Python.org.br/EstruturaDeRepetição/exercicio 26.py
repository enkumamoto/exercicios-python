'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.
'''

print('Eleições da marmelada')
qtd_eleitores = int(input('Digite a quantidade de eleitores:'))
votos = []

for x in range(qtd_eleitores):
    urna = votos.append(int(input('Para que vai seu voto? [1, 2 ou 3]: ')))

print('Quantidade do votos para o Candidato 1:',votos.count(1))
print('Quantidade do votos para o Candidato 2:',votos.count(2))
print('Quantidade do votos para o Candidato 3:',votos.count(3))