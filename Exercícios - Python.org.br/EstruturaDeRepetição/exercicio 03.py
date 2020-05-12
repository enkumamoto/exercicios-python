'''
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: s's', 'c', 'v', 'd';
'''
nome = str(input('Digite seu nome: '))
while ( len(nome) <=  3 ):
    print ('ERRO: Campo Nome possui 3 ou menos caracteres. Nome deve conter mais de 3 caracteres.')
    nome = str(input('Digite seu nome: '))

idade = int(input('Digite sua idade: '))
while idade > 150 or idade < 0:
    print ('ERRO: Idade inválida. Idade de ser entre 0 e 150.')
    idade = int(input('Digite sua idade: '))

salario = float(input('Digite seu salário (Ex.: R$1234.56): R$'))
while salario < 0:
    print ('ERRO: Salário menor ou igual a R$0,00. Salário deve ser maior que R$0,00')
    salario = float(input('Digite seu salário (Ex.: R$1234.56): R$'))

sexo = str(input('Digite seu sexo (m ou f): '))
while sexo != 'm' and sexo != 'f':
    print('ERRO: Opção invalida. Por favor, insira uma das opções informadas')
    sexo = str(input('Digite seu sexo (m ou f): '))

civil = str(input('Digite seu Estado Civil usando:\n"s" para Solteiro\n"c" para Casado\n"v" para Viúvo\n"d" para Divorciádo\nDigite aqui a opção escolhida:'))
while civil != 's' and civil != 'v' and civil != 'c' and civil != 'd':
    print('ERRO: Opção invalida. Por favor, insira uma das opções informadas')
    civil = str(input('Digite seu Estado Civil usando:\n"s" para Solteiro\n"c" para Casado\n"v" para Viúvo\n"d" para Divorciádo\nDigite aqui a opção escolhida:'))

else:
    print('Todas as informações estão corretas.')