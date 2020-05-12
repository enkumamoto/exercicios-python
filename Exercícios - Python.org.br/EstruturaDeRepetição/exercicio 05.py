'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
'''
import os

while True:
    pais_A = int(input('Digite a população de um local A: '))
    tx_crescimento_A = float(input('Digite uma taxa de crescimento do local A:'))
    pais_B = int(input('Digite a população de um local B: '))
    tx_crescimento_B = float(input('Digite uma taxa de crescimento do local B:'))

    txcA = float(tx_crescimento_A / 100)
    txcB = float(tx_crescimento_B / 100)

    year = 0

    while pais_A <= pais_B:
        pais_A = pais_A + (pais_A * txcA)
        pais_B = pais_B + (pais_B * txcB)
        year += 1

    print('A população do Local A ultrapassará ou será igual do Local B em %d anos.' % year)

    repetir = input('Gostaria de repetir a operação? [S]im ou [N]ão: ').lower()
    if repetir == 'n':
        print('Até logo!')
        break

    else:
        continue
 