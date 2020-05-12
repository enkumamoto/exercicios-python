'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai
utilizar o sistema. Após todos os alunos terem respondido informar:

    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.

    Gabarito da Prova:

    01 - A
    02 - B
    03 - C
    04 - D
    05 - E
    06 - E
    07 - D
    08 - C
    09 - B
    10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos
alunos usarem o programa.
'''
print ('Cartão de Respostas e Gabarito')
gabarito = []
resp_alunos = []
notas_tiradas = []
print('Professor: ')
qtd_quetoes = int(input('Digite a quantidade de questões da sua prova: '))

for x in range(qtd_quetoes):
    print('Questão', x + 1)
    resp_correta = gabarito.append(input('Digite a Resposta Correta: '))

num_aluno = 1
continuar = True

while continuar != 'n':
    print('\n' * qtd_quetoes)
    print('Aluno nº',num_aluno,':')
    resp_alunos.clear()
    for x in range(qtd_quetoes):
        print('Questão', x + 1)
        resp_alunos.append(input('Digite a sua resposta: '))
    nota = 0

    for x in range(qtd_quetoes):
        if resp_alunos [x] == gabarito[x]:
            nota += 1

    notas_tiradas.append(nota)
    continuar = input('Outro aluno utilizará o sistema? (S/N)')
    num_aluno += 1

media = sum(notas_tiradas) / len(notas_tiradas)

print(len(notas_tiradas),"alunos utilizaram o sistema.")
print('A maior nota é:',max(notas_tiradas))
print('A menor nota é:',min(notas_tiradas))
print('A média da turma é: %.2f'%media)
print(notas_tiradas)
