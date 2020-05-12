'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.
'''

print('Checagem de login e senha!')
name = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

while name == senha:
    print('Erro: Usuário e senha iguais, dados devem ser diferentes.')
    nome = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
else:
    print('Cadastro realizado com sucesso!')