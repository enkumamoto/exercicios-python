'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno
mais alto e o número do aluno mais baixo, junto com suas alturas.
'''
num_aluno = []
alt_aluno = []

for x in range(10):
    print ('Aluno nº',x + 1,':')
    aluno = int(input('Digite o número do aluno: '))
    while aluno in num_aluno:
        print('Número do aluno já foi usado.')
        aluno = int(input('Digite o número do aluno: '))
    altura = alt_aluno.append(float(input('Digite a altura do aluno: ')))
    num_aluno.append(aluno)

print('O maior número de aluno:',max(num_aluno))
print('O aluno mais alto tem:',max(alt_aluno))

print('O menor número de aluno:',min(num_aluno))
print('O aluno mais baixo tem:',min(alt_aluno))