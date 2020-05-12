'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''
print('Média da Faixa Etária da População')
total_pesquisados = []
qtd_pop = int(input('Digite a quantidade de pessoas:'))

for x in range(qtd_pop):
    idade = total_pesquisados.append(int(input('Digite sua idade: ')))

if sum(total_pesquisados) / len(total_pesquisados) < 25:
    print ('Média de idade considera a turma jovem.')

elif sum(total_pesquisados) / len(total_pesquisados) >= 25 and sum(total_pesquisados) / len(total_pesquisados) < 60:
    print ('Média de idade considera a turma adulta.')

else:
    print ('Média de idade considera a turma idosa.')