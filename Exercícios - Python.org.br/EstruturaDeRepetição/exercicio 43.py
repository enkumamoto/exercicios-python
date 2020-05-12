'''
O cardápio de uma lanchonete é o seguinte:

    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por
item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''
print ('Bem vindo ao Porco Sebosão')
print ('O cardápio de uma lanchonete é o seguinte:\n\nEspecificação   Código  Preço\nCachorro Quente 100     R$ 1,20\nBauru Simples   101     R$ 1,30\nBauru com ovo   102     R$ 1,50\nHambúrguer      103     R$ 1,20\nCheeseburguer   104     R$ 1,30\nRefrigerante    105     R$ 1,00')

lanches = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hambúrguer', 'Cheeseburguer', 'Refrigerante']
cod_lanche = [100,101,102,103,104,105]
vlr_lanche = [1.20,1.30,1.50,1.20,1.30,1.00]
codigo = True
n_pedido = 1
pedido = []

print('Quando encerrar suas escolhas, digite 0.')

while codigo != 0:
    print(f"Pedido nº: {n_pedido}")
    codigo = int(input('Digite o código do produto: '))
    if codigo == 0:
        break
    else:
        while codigo not in cod_lanche:
            print('Código inválido. Utilize um dos códigos da tabela:')
            print('Especificação   Código  Preço\nCachorro Quente 100     R$ 1,20\nBauru Simples   101     R$ 1,30\nBauru com ovo   102     R$ 1,50\nHambúrguer      103     R$ 1,20\nCheeseburguer   104     R$ 1,30\nRefrigerante    105     R$ 1,00')
            codigo = int(input('Digite o código do produto: '))
        indice = cod_lanche.index(codigo)
        qtd_lanche = int(input('Digite a quantidade do produto: '))
        vlrr_lanche = vlr_lanche[indice] *1
        total_pedido = vlrr_lanche * qtd_lanche
        print('Valor unitário: R$%.2f - Quantidade: %.2f\nTotal: R$%.2f'%(vlrr_lanche, qtd_lanche, total_pedido))

        pedido.append(total_pedido)
    n_pedido =+ 1

pedido_nota = 0

for x in range(n_pedido - 1):
    print('Pedido nº',pedido_nota + 1,'\nR$',round(pedido(pedido_nota,2)))
    pedido_nota += 1

total_geral = sum(pedido)
print('Total a pagar: R$%.2f'%total_geral)