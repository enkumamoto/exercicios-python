'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não
é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
'''
print("Calculo Salarial")

print('Programa para Calculo de Descontos Salarial')
vht = float(input('Para começar digite o valor da hora de trabalho: R$'))
qht = int(input('Informe a quantidade de horas trabalhadas: '))

pctinss = '10%'
pctfgts = '11%'
income = vht * qht
INSS = income * 0.10
IRISENTO = 0
IR5 = income * 0.05
IR10 = income * 0.10
IR20 = income * 0.20
FGTS = income * 0.11
SIND = income * 0.03
SLR = income + IRISENTO + FGTS - INSS
TDS = INSS
TDS5 = IR5 + INSS
TDS10 = IR10 + INSS
TDS20 = IR20 + INSS
SLR5 = income - TDS5 + FGTS
SLR10 = income - TDS10 + FGTS
SLR20 = income - TDS20 + FGTS

if income <= 900:
    print(f'+ Salário Bruto ({vht} * {qht} )...: R${income}')
    print('- Imp. de Renda.................: Isento.')
    print('- Contrib. INSS ' + str(pctinss) + '.............: R$%.2f'%INSS)
    print('+ Contrib. FGTS ' + str(pctfgts) + '.............: R$%.2f'%FGTS)
    print('  Sindicato (Pago pela Empresa).: R$%.2f' % SIND)
    print('- Desconto Total................: R$%.2f' % TDS)
    print('= Salário Líquido...............: R$%.2f' % SLR)

elif income > 900 and income <=1500:
    print(f'+ Salário Bruto ({vht} * {qht} )...: R${income}')
    print('- Imp. de Renda.................: R$%.2f'%IR5)
    print('- Contrib. INSS ' + str(pctinss) + '.............: R$%.2f' % INSS)
    print('+ Contrib. FGTS ' + str(pctfgts) + '.............: R$%.2f' % FGTS)
    print('  Sindicato (Pago pela Empresa).: R$%.2f' % SIND)
    print('- Desconto Total................: R$%.2f' % TDS5)
    print('= Salário Líquido...............: R$%.2f' % SLR5)

elif income >1500 and income <=2500:
    print(f'+ Salário Bruto ({vht} * {qht} )...: R${income}')
    print('- Imp. de Renda.................: R$%.2f'%IR10)
    print('- Contrib. INSS ' + str(pctinss) + '.............: R$%.2f' %INSS)
    print('+ Contrib. FGTS ' + str(pctfgts) + '.............: R$%.2f'%FGTS)
    print('  Sindicato (Pago pela Empresa).: R$%.2f' % SIND)
    print('- Desconto Total................: R$%.2f' % TDS10)
    print('= Salário Líquido...............: R$%.2f' % SLR10)

elif income > 2500:
    print(f'+ Salário Bruto ({vht} * {qht} )...: R${income}')
    print('- Imp. de Renda.................: R$%.2f'%IR20)
    print('- Contrib. INSS ' + str(pctinss) + '.............: R$%.2f' %INSS)
    print('+ Contrib. FGTS ' + str(pctfgts) + '.............: R$%.2f' %FGTS)
    print('  Sindicato (Pago pela Empresa).: R$%.2f' %SIND)
    print('- Desconto Total................: R$%.2f' %TDS20)
    print('= Salário Líquido...............: R$%.2f' %SLR20)

else:
    print ('Dados inválidos.')
