'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
'''


qtd_temps = int(input('Quantidade de temperaturas para análise: '))

qtd_temp = 1
temperaturas = []
n_temp = temperaturas.__len__()

for x in range(qtd_temps):
    print('Temperatura nº',qtd_temp)
    temp = temperaturas.append(float(input('Digite a temperatura em ºC: ')))
    qtd_temp += 1

media = sum(temperaturas) / qtd_temps
media = media.__round__()

print('A temperatura máxima é:', max(temperaturas))
print('A temperatura mínima é:', min(temperaturas))
print(f'A temperatura média é: {media}')