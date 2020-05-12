'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''
altura = float(input('Digite sua altura, exemplo (1.68): '))

homens = (72.7*altura) - 58
mulheres = (62.1*altura) - 44.7

print (f'Se você é mulher seu peso ideal é: %.1fkg'%mulheres)
print (f'Se você é homen seu peso ideal é: %.1fkg'%homens)