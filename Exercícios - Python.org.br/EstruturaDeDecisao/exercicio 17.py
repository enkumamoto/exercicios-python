'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
'''
print ('É ou não é bi?')
ano = int(input('Digite o ano parasaber se é ou não bissexto: '))

# se ano divisivel por 4 (resta 0) e divisivel por 100 (resto diferente de 0) ou divisivel por 400 (restando 0)
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print ('O ano é bissexto!')

else:
    print('O ano não é bissexto!')