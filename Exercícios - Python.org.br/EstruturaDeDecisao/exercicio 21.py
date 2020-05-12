'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 2, 5, 10 , 20, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e
    uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de
    10, uma nota de 5 e quatro notas de 1.
'''
print ('Money que é good! E nois num have!')
value = eval(input('Digite quanto quer sacar: R$'))

cem = cinquenta = vinte = dez = cinco = dois = um = 0

value = float("%.2f" % value)
if int(value/100) >= 1:
	cem = int(value/100)
	value -= cem*100

value = float("%.2f" % value)
if int(value/50) >= 1:
	cinquenta = int(value/50)
	value -= cinquenta*50

value = float("%.2f" % value)
if int(value/20) >= 1:
	vinte = int(value/20.00)
	value -= vinte*20

value = float("%.2f" % value)
if int(value/10) >= 1:
	dez = int(value/10)
	value -= dez*10.00

value = float("%.2f" % value)
if int(value/5) >= 1:
	cinco = int(value/5)
	value -= cinco*5

value = float("%.2f" % value)
if int(value/2) >= 1:
	dois = int(value/2)
	value -= dois*2

value = float("%.2f" % value)
if int(value/1) >= 1:
	um = int(value/1)
	value -= um*1

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % cem)
print("%d nota(s) de R$ 50.00" % cinquenta)
print("%d nota(s) de R$ 20.00" % vinte)
print("%d nota(s) de R$ 10.00" % dez)
print("%d nota(s) de R$ 5.00" % cinco)
print("%d nota(s) de R$ 2.00" % dois)
print("%d moeda(s) de R$ 1.00" % um)