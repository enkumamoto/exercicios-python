''''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
print('Programa para Calculo de Descontos Salarial')
vht = float(input('Para começar digite o valor da hora de trabalho: R$'))
qht = int(input('Informe a quantidade de horas trabalhadas: '))

income = vht * qht
IR = income * 0.11
INSS = income * 0.08
SIND = income * 0.05
TDS  = IR + INSS + SIND
SLR = income - TDS

print (f'+ Salário Bruto  : R${income}')
print ("- Imp. de Renda  : R$%.2f"%IR)
print ('- Contrib. INSS  : R$%.2f'%INSS)
print ('- Sindicato      : R$%.2f'%SIND)
print ('- Desconto Total : R$%.2f'%TDS)
print ('= Salário Líquido: R$%.2f'%SLR)
