'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool,
G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o
preço do litro do álcool é R$ 1,90.
'''
print('Combustível até o talo!')
print('\n')
print('Olá! Você abasteceu seu veículo no nosso posto.\nPor favor infome digitando:')
combustivel = input('Use G para Gasolina\nUse A para Álcool\nDigite a opção desejada: ').lower()

gasolina = 2.50
alcool = 1.90
desc_alcool1 = (alcool * 0.03)
desc_alcool2 = (alcool * 0.05)
desc_gasolina1 = (gasolina * 0.04)
desc_gasolina2 = (gasolina * 0.06)

if combustivel == 'a':
    qtdcombustivel = float(input('Ok, você abasteceu o veículo com álcool.\nPor favor informe a quantidade em litros: '))
    if qtdcombustivel <= 20:
        total_sem_desc1 = (qtdcombustivel * alcool)
        total_pgto = total_sem_desc1 - desc_alcool1
        print(f'Total em litros: {qtdcombustivel}L')
        print('Valor do Álcool/L: R$%.2f'%alcool)
        print('Total sem desconto: R$%.2f'%total_sem_desc1)
        print('Valor do desconto: R$%.2f'%desc_alcool1)
        print('Total a pagar: R$%.2f'%total_pgto)
    
    if qtdcombustivel > 20:
        total_sem_desc2 = (qtdcombustivel * alcool)
        total_pgto = total_sem_desc2 - desc_alcool2
        print(f'Total em litros: {qtdcombustivel}L')
        print('Valor do Álcool/L: R$%.2f'%alcool)
        print('Total sem desconto: R$%.2f'%total_sem_desc2)
        print('Valor do desconto: R$%.2f'%desc_alcool2)
        print('Total a pagar: R$%.2f'%total_pgto)

elif combustivel == 'g':
    qtdcombustivel = float(input('Ok, você abasteceu o veículo com gasolina.\nPor favor informe a quantidade em litros: '))
    if qtdcombustivel <= 20:
        total_sem_desc3 = (qtdcombustivel * gasolina)
        total_pgto = total_sem_desc3 - desc_gasolina1
        print(f'Total em litros: {qtdcombustivel}L')
        print('Valor do Álcool/L: R$%.2f'%gasolina)
        print('Total sem desconto: R$%.2f' % total_sem_desc3)
        print('Valor do desconto: R$%.2f'%desc_gasolina1)
        print('Total a pagar: R$%.2f'%total_pgto)
    
    if qtdcombustivel > 20:
        total_sem_desc4 = (qtdcombustivel * gasolina)
        total_pgto = total_sem_desc4 - desc_gasolina2
        print(f'Total em litros: {qtdcombustivel}L')
        print('Valor do Álcool/L: R$%.2f'%gasolina)
        print('Total sem desconto: R$%.2f' % total_sem_desc4)
        print('Valor do desconto: R$%.2f'%desc_gasolina2)
        print('Total a pagar: R$%.2f'%total_pgto)

else:
    print ('Dados inválidos.')