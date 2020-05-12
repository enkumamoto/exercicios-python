'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
print ('Vogal o Consoante')

letra = input ('Digite qualquer letra: ')

vogais = ('a','e','i','o','u')

if letra in vogais:
    print (f'A letra {letra} é uma vogal!')

else:
    print (f'A letra {letra} é uma consoante!')