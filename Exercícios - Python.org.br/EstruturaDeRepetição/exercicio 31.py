'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final
da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
a próxima compra. A saída deve ser conforme o exemplo abaixo:

    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
    ...
'''
import time

print ('Lojas do Manoel')

while True:
    produtos = []
    counter = 1
    valor_produto = True

    while valor_produto != 0:
        print("Produto n°",counter)
        valor_produto = float(input('Digite o preço do produto: R$ '))
        produtos.append(valor_produto)
        counter += 1

    print('Total: R$%.2f'%(sum(produtos)))
    dinheiro = float(input('Digite quanto irá pagar: R$'))

    while dinheiro < sum(produtos):
        print('Valor de pagamento abaixo do total, o valor oferecido deve ser igual ou maior que o total.')
        dinheiro = float(input('Digite quanto irá pagar: R$'))

    troco = dinheiro - sum(produtos)

    print(f'Dinheiro: R${dinheiro}')
    print('Troco: R$%.2f'%troco)
    print("\nPróxima compra em 5 segundos")
    time.sleep(5)
    print('\n' * 5)