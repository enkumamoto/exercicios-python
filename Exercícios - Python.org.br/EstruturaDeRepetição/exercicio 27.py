'''
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
'''
print('O colégio está cheio?')

turmas = int(input('Digite a quantidade de turmas: '))
alunos_turma = []
turma = 1

for x in range(turmas):
    print("Turma", turma)
    alunos = int(input('Alunos da turma: '))

    while alunos > 40:
        print ('Turma', turma,"[Uma turma só pode ter 40 alunos.]")

        alunos = int(input('Alunos da turma: '))

    turma += 1
    alunos_turma.append(alunos)

media_turma = sum(alunos_turma) / len(alunos_turma)
media = media_turma.__round__()
print(f'A media por turma é de {media} alunos por turma.')