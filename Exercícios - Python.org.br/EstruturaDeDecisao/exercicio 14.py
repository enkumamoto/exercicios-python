'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
    for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

print ('Checagem das médias escolares.')
print ('Verifique se você foi aprovado ou reprovado.')

nota1 = float(input('Digite a primeira nota (Exemplo: 8.6): '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media == 10 and media > 9:
    print('Sua média é %.1f. Aprovado com conceito A! =D, %media')

elif media > 7.5 and media <=9:
    print('Sua média é %.1f, Parabéns, você foi aprovado com conceito B! =)' %media)

elif media > 6 and media <=7.5:
    print('Sua média é %.1f, Parabéns, você foi aprovado com conceito C! =)' %media)

elif media > 4 and media <=6:
    print('Sua média é %.1f, Você foi reprovado com conceito D... =(' %media)

elif media > 0 and media <=4:
    print('Sua média é %.1f, Você foi reprovado com conceito E... =(' %media)

else:
    print('Dados inválidos.')
