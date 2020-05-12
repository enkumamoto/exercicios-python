'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
'''
print ('A potência!')
while True:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número para ser o expoente: '))
    res = num1 ** num2
    print(f'{num1} elevado a {num2} resulta no valor: {res}')

    repetir = input('Gostaria de repetir a operação? [S]im ou [N]ão: ').lower()
    if repetir == 'n':
        print('Até logo!')
        break

    else:
        continue