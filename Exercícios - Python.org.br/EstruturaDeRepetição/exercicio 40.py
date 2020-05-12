'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''
print('Departamento Nacional de Transito\nGerador de Relatório.\nInsira os dados:')

cod_cidades = []
num_carro_passeio = []
num_acdnt_vitima = []
acdnt_2000 = []

for x in range(5):
    print('\nCidade nº:', x + 1)
    codigo_cidade = int(input('Digite o Código da Cidade: '))

    while codigo_cidade in cod_cidades:
        print('Este codigo de cidade já foi usado.')
        codigo_cidade = int(input('Digite o Código da Cidade: '))

    carro = int(input('Digite a quantidade de carros: '))
    acidente = int(input('Digite a quantidade de acidentes com vítimas: '))

    if carro > 2000:
        acdnt_2000.append(carro)
        num_acdnt_vitima.append(acidente)
    else:
        num_acdnt_vitima.append(acidente)

    num_carro_passeio.append(carro)
    cod_cidades.append(codigo_cidade)

menor_indice_acdnt = num_acdnt_vitima.index(min(num_acdnt_vitima))
maior_indice_acdnt = num_acdnt_vitima.index(max(num_acdnt_vitima))
print('Relatório:\n')
print('\nMenor índice de acidente\nQuantidade de acidentes:',min(num_acdnt_vitima),'\nPertence a cidade do cód.:',cod_cidades[menor_indice_acdnt])
print('\nMaior índice de acidente\nQuantidade de acidentes:',max(num_acdnt_vitima),'\nPertence a cidade do cód.:',cod_cidades[maior_indice_acdnt])
print('\n')
med_carros = sum(num_carro_passeio) / num_carro_passeio.__len__()
print(f'A média de carros das 5 cidades é de {med_carros}')
print('\n')
med_acdnt_2000 = sum(acdnt_2000) / acdnt_2000.__len__()
print(f'A média de acidentes em cidades com menos de 2000 carros é de {med_acdnt_2000}')