'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

    Exemplo:

      12376489
      => 98467321
'''

while True:
    seq = input("Digite uma sequência de números: ")

    if seq == "":
        print('Nada foi digitado.')
        seq = input("Digite uma sequência de números: ")
    else:
        print('Número invertido:',seq[::-1])
        break
