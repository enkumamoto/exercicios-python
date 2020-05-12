'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta,
o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer
um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos
conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para
armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado
quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''
print ('Olimpíadas da Comunidade Pernetas do Amanhã')

nome_atleta = True
num_atleta = 1
while nome_atleta != '':
    saltos = []
    print('Atleta nº:',num_atleta)
    nome_atleta = input('Digite o nome do atleta: ')
    if nome_atleta == '':
        break

    else:
        num_salto = 1
        for x in range(5):
            print('Salto nº',num_salto)
            dist_salto = float(input('Digite a distancia do salto: '))
            saltos.append(dist_salto)
            num_salto += 1
        print(f'Atleta: {nome_atleta}')
        num_salto = 1
        count = 0

        for x in range(5):
            print(num_salto,'° Salto:',saltos[count],'m')
            num_salto += 1
            count += 1
        print('Melhor salto:',max(saltos),'m')
        print('Pior salto:', min(saltos), 'm')

        saltos.remove(max(saltos))
        saltos.remove(max(saltos))
        media = sum(saltos) / len(saltos)
        media = round(media,2)
        print(f'Média do demias saltos: {media}m')
        print(f'Resultado Final:\n{nome_atleta}: {media}m')

        novo = input('Informará novo atleta? (S/N):')
        if novo == 'n':
            break
        else:
            num_atleta +=1