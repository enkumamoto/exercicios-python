'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

print ('Checagem das médias escolares.')
print ('Verifique se você foi aprovado ou reprovado.')

nota1 = float(input('Digite a primeira nota (Exemplo: 8.6): '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
media = float(media)

if media == 10:
    print(f'Sua média é {media}. Aprovado com Distinção! =D')

elif media >= 7:
    print(f'Sua média é {media}. Parabéns, você foi aprovado! =)')

else:
    print(f'Sua média é {media}. Você foi reprovado... =(')