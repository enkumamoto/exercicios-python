'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
valor seja maior que 500.
'''
print('Gerador Fibonacci!')

limite = int(input('Digite o número máximo para sequência: '))
ultimo = 1
penultimo = 0
termo = 0

while termo <= limite:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    print(termo)