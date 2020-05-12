'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino,
 Sexo Inválido.
'''
print('Olha embaixo da toalha!')
sexo = input('Digite seu sexo: ').lower()

if sexo == 'f':
    print ('Feminino')

elif sexo == 'm':
    print ('Masculino')

elif sexo == 'traveco da rolona':
    print ('Cadê o Lucas?')

else:
    print('Sexo Inválido ou indefinido.')