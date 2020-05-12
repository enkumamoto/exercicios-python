'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''
print('Coleção de CDs')

qtd_cds = int(input('Digite a quantidade de CDs: '))
cds = []
counter = 1

for x in range(qtd_cds):
    print("CD", counter)
    valor_cd = float(input('Informe o valor do CD: R$'))
    counter += 1
    cds.append(valor_cd)

media_cd = sum(cds) / len(cds)
valor_total_colecao = sum(cds)

print('Sua coleção contém:\n'+len(cds)+' Cds\nO valor total da coleção é: R$%.2f\nO custo médio por CD é de: R$%.2f'%(valor_total_colecao,media_cd))