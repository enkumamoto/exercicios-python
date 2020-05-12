'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário,
conforme exemplo abaixo:

    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7

    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35

Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''
import time
print('Eca... Tabuada Montada, mas simplificada...')

multi = int(input('Digite o número da tabuada que deseja visualizar: '))
inicio = int(input('Digite onde a tabuada inicia: ' ))
final = int(input('digite onde a tabuada finaliza: '))


if inicio > final:
    print('O número de início da tabuada deve ser menor que o número final.\nPrograma finalizado.')
else:
    print(f'Montar a tabuada de: {multi}\nComeçar por: {inicio}\nTerminar em: {final}\n')
    time.sleep(3)
    print(f'Vou montar a tabuada de {multi} começando em {inicio} e terminando em {final}:')

    for n in range(inicio,final + 1):
        res = n * multi
        print(f'{n} x {multi} = {res}')
        n += 1
