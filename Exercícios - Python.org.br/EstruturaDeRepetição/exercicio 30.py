'''
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um
sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães,
de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

    Preço do pão: R$ 0.18
    Panificadora Pão de Ontem - Tabela de preços
    1 - R$ 0.18
    2 - R$ 0.36
    ...
    50 - R$ 9.00
'''
print('Panificadora Pão de Ontem')

qtd_paes = int(input('Digite a quantidade de pães: '))
preco_pao = float(input('digite o valor do pão: R$'))

while qtd_paes > 50 or qtd_paes < 0:
    print('Quantidade de pães acima do permitido. Por favor, digite uma quantidade até 50:')
    qtd_paes = int(input('Digite a quantidade de pães: '))

for x in range(qtd_paes):
    x = qtd_paes * preco_pao

print('Total a pagar é: R$%.2f'%x)