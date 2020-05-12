'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
print ('Checagem das médias escolares.')
print ('Verifique se você foi aprovado ou reprovado.')

nota1 = float(input('Digite a primeira nota (Exemplo: 8.6): '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media == 10:
    print(f'Sua média é {media}. Aprovado com Distinção! =D')

elif media >= 7:
    print(f'Sua média é {media}. Parabéns, você foi aprovado! =)')

else:
    print(f'Sua média é {media}. Você foi reprovado... =(')