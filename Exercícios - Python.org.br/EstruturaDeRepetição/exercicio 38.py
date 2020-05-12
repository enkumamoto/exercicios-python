'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

    Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.

Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o
usuário digite o salário inicial do funcionário.
'''
print('Olha o aumento do salário!!!!')
tx_aumento = 0.15
salario = float(input('Digite o valor do seu salário: R$'))
ano = int(input('Digite o ano atual: '))

for x in range (1996, ano + 1):
    salario_atual = salario + (salario * tx_aumento)
    tx_aumento *= 2
    print('Seu slario em:',x,'é de: R$%.2f'%salario_atual)
