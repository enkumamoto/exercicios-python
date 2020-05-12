'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua
nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos
sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''
print ('Olimpíadas da Comunidade Pernetas do Amanhã')

nome_atleta = True
num_atleta = 1
while nome_atleta != '':
    notas = []
    print('Atleta nº:',num_atleta)
    nome_atleta = input('Digite o nome do atleta: ')
    if nome_atleta == '':
        break

    else:
        num_nota = 1
        for x in range(7):
            print('Nota nº',num_nota)
            dist_salto = float(input('Digite a nota: '))
            notas.append(dist_salto)
            num_nota += 1
        print(f'Atleta: {nome_atleta}')
        num_nota = 1
        count = 0

        for x in range(7):
            print(num_nota,'° Nota:',notas[count],)
            num_nota += 1
            count += 1

        print('Resultado final:')
        print('Melhor Nota:', max(notas))
        print('Pior Nota:', min(notas))
        notas.remove(max(notas))
        notas.remove(min(notas))
        media = sum(notas) / len(notas)
        media = round(media, 2)
        print(f'Média do demias notas: {media}')
        # print(f'Resultado Final:\n{nome_atleta}: {media}')

        novo = input('Informará novo atleta? (S/N):')
        if novo == 'n':
            break
        else:
            num_atleta +=1