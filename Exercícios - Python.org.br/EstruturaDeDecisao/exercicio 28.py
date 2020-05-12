'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites
para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5%
sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom
fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e
valor a pagar.
'''

def calcular_precos():
    count = 0
    calculo_produto = 0
    dados_produto = [('file duplo', 4.90, 5.80), ('alcatra', 5.90, 6.80), ('picanha', 6.90, 7.80)]
    while True:
        finalizar = False
        produto = input("Por favor, informe o produto desejado(Filé Duplo, Alcatra ou Picanha):")
        for x in range(3):
            if produto.lower() == dados_produto[x][0]:
                count = x
                finalizar = True
                break
            else:
                if x == 2:
                    finalizar = False
                    print('Valor inválido.', produto)
        if finalizar:
            break
    while True:
        try:
            peso = float(input('Por favor, informar o peso desejado:'))
            if peso > 0:
                break
            else:
                continue
        except ValueError:
            print('Valor do peso é inválido.')
    if peso <= 5 and peso > 0:
        pgto_form = input('Estamos em prmoção, pagando com Cartão Tabaljara ganha 5% de desconto!\nDeseja pagar com o Cartão Tabajara S ou N? ').lower()
        if pgto_form == 'n':
            calculo_produto = dados_produto[count][1] * peso
            print("Valor a pagar:R$%.2f" % calculo_produto)
        else:
            calculo_produto = dados_produto[count][1] * peso
            valor_desc = (calculo_produto * 0.05)
            calculo_produto_desc = calculo_produto - valor_desc
            print("Valor a pagar: R$%.2f\nVocê ganhou R$%.2f de desconto!" % (calculo_produto_desc, valor_desc))
    elif peso > 5:
        pgto_form = input('Estamos em prmoção, pagando com Cartão Tabaljara ganha 5% de desconto!\nDeseja pagar com o Cartão Tabajara S ou N? ').lower()
        if pgto_form == 'n':
            calculo_produto = dados_produto[count][2] * peso
            print("Valor a pagar:R$%.2f"%calculo_produto)
        else:
            calculo_produto = dados_produto[count][2] * peso
            valor_desc = (calculo_produto * 0.05)
            calculo_produto_desc = calculo_produto - valor_desc
            print("Valor a pagar: R$%.2f\nVocê ganhou R$%.2f de desconto!" % (calculo_produto_desc, valor_desc))
calcular_precos()