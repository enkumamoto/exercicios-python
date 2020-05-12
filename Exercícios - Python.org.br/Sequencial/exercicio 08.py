print("Oh o salário!")
print()
print('Para calcular o seu salário do mês precisamos de algumas informações.')
vht = float(input('Informe o valor da sua hora de trabalho: '))
qht = float(input('Informe a quantidade de horas trabalhadas: '))
print()

income = vht * qht

print(f'Neste mês você trabalhou {qht}hr pelo valor de R${vht}/hora, recebendo o total: R${income}')
