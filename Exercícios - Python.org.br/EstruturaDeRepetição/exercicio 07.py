'''
Faça um programa que leia 5 números e informe o maior número.
'''
print('Digite 5 números e informo o maior número')
lista = []
while len(lista) < 5:
    num = int(input('Digite um número (para finalizar digite 0): '))
    lista.append(num)

print ('O maior número é:',max(lista))
