"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5%
    Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""

print ("Olha o aumentoooooo!")
print("\n")
income = float(input("Digite salário atual (Ex.: 123.45): R$ "))

r1 = "20%"
r2 = "15%"
r3 = "10%"
r4 = "5%"

plus1 = float(income) * 0.20
plus2 = float(income) * 0.15
plus3 = float(income) * 0.10
plus4 = float(income) * 0.05

aumento1 = float(income + plus1)
aumento2 = float(income + plus2)
aumento3 = float(income + plus3)
aumento4 = float(income + plus4)

if income <= 280:
    print("O salário antes do reajuste: R$"+str(income)+"\nO percentual de aumento aplicado: "+r1+"\nO valor do aumento: R$%.2f\nO novo salário, após o aumento: R$%.2f"%(plus1, aumento1))

elif income <= 700 and income > 280:
    print("O salário antes do reajuste: R$"+str(income)+ "\nO percentual de aumento aplicado: "+r2+"\nO valor do aumento: R$%.2f\nO novo salário, após o aumento: R$%.2f"%(plus2, aumento2))

elif income < 1500 and income > 700:
    print("O salário antes do reajuste: R$"+str(income)+ "\nO percentual de aumento aplicado: "+r3+"\nO valor do aumento: R$%.2f\nO novo salário, após o aumento: R$%.2f"%(plus3, aumento3))

elif income >= 1500:
    print("O salário antes do reajuste: R$"+str(income)+ "\nO percentual de aumento aplicado: "+r4+"\nO valor do aumento: R$%.2f\nO novo salário, após o aumento: R$%.2f"%(plus4, aumento4))

else:
    print('Valor inválido.')