
'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
'''
def decint ():
    if num1 == 0:
        return 'Oh, ¬¬ o zero não vale...'

    elif num1 == round(num1):
        return f'O {num1} é inteiro'

    else:
        return f'O {num1} é Decimal'

def parimpar ():
    if num1 == 0:
        return 'Oh, ¬¬ o zero não vale...'

    elif (num1 % 2) == 0:
        return f'O {num1} é  par.'

    else:
        return f'O {num1} é  ímpar.'

def posneg ():
    if num1 == 0:
        return 'Oh, ¬¬ o zero não vale...'

    elif num1 > 0:
        return f'O {num1} é positivo! :)'

    else:
        return f'O {num1} é negativo! :)'

print ('O que danado você quer?')
print ('Primeiro escolha dois números')
num2 = float(input('Digite o primeiro número: '))
num3 = float(input('Digite o segundo número: '))
num1 = 0
print('\n')

print('Agora escolha que operação matemática quer realizar.')
operacao = int(input('Digite:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nDigite a opção: '))
if operacao == 1:
    num1 = num2 + num3

    print(parimpar())
    print(posneg())
    print(decint())


elif operacao == 2:
    num1 = num2 - num3
    print(parimpar())
    print(posneg())
    print(decint())

elif operacao == 3:
    num1 = num2 * num3
    print(parimpar())
    print(posneg())
    print(decint())

elif operacao == 4:
    num1 = num2 / num3
    print(parimpar())
    print(posneg())
    print(decint())

else:
    print ('Dados inválidos.')