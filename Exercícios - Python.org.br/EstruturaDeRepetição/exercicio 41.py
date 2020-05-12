'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:

    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1                       0
    3                       10
    6                       15
    9                       20
    12                      25

Exemplo de saída do programa:

    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     10              3                       R$    366,00
    R$ 1.150,00     15              6                       R$    191,67
'''

print('Parcelamos dívida!')

debt = float(input('Digite o valor da sua dívida: R$'))
parc = int(input('Digite o número de parcelas: '))
juros1 = '0'
juros3 = '10'
juros6 = '15'
juros9 = '20'
juros12= '25'
x = 0

while True:
    while parc > 12:
        print ('Número de parcelas solicitadas é superior a 12 parcelas')
        parc = int(input('Digite o número de parcelas: '))
    if parc <=2 and parc == 0:
        vl_prc = round(debt,2)
        print(f'Valor da Dívida: R${debt}\nValor dos Juros:{juros1}%\nQuantidade de Parcelas: {parc}\nValor da Parcela: R${vl_prc}')
        break

    elif parc >= 3 and parc <= 5:
        vl_prc = round((debt+ (debt * 0.1)) / parc,2)
        print(f'Valor da Dívida: R${debt}\nValor dos Juros:{juros3}%\nQuantidade de Parcelas: {parc}\nValor da Parcela: R${vl_prc}')
        break

    elif parc >= 6 and parc <= 8:
        vl_prc = round((debt+ (debt * 0.15)) / parc,2)
        print(f'Valor da Dívida: R${debt}\nValor dos Juros:{juros6}%\nQuantidade de Parcelas: {parc}\nValor da Parcela: R${vl_prc}')
        break

    elif parc >= 9 and parc <= 11:
        vl_prc = round((debt+ (debt * 0.20)) / parc,2)
        print(f'Valor da Dívida: R${debt}\nValor dos Juros:{juros9}%\nQuantidade de Parcelas: {parc}\nValor da Parcela: R${vl_prc}')
        break

    elif parc == 12:
        vl_prc = round((debt+ (debt * 0.25)) / parc,2)
        print(f'Valor da Dívida: R${debt}\nValor dos Juros:{juros12}%\nQuantidade de Parcelas: {parc}\nValor da Parcela: R${vl_prc}')
        break
