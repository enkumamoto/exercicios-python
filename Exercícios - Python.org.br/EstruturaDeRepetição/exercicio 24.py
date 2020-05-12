'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''
print('Média aritimetica dos alunos')
num_notas = int(input('Digite a quantidade de notas que gostaria de calcular: '))
count = 0
todas_notas = []

while num_notas > count:
    notas = todas_notas.append(float(input('Digite a nota: ')))
    count += 1

media = sum(todas_notas) / num_notas
print ('A média aritimética é: %.2f'%media)