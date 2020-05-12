'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
'''
print('Eca... Tabuada!')

multi = int(input('Digite o número da tabuada que deseja visualizar: '))
print(f'A tabuada do numero {multi}:')

for n in range(1,11):
    res = n * multi
    print(f'{n} x {multi} = {res}')
    n += 1