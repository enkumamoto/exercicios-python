'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também
deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das
alturas e dos pesos dos clientes
'''
# O texto da questão parece meio confuso, mas colocarei comentário para ajudar na resolução.
# Para ficar mais amigável
print('Academia Maromba Frenética!\n Estamos realizando um senso na nossa academia.\nGostaríamos que nos informasse alguns dados:')
# Para guardar os dados do senso, criaremos 3 listas.
cod_clientes = []
altura_clientes = []
peso_clientes = []

# Início do contador
n_cliente = 1

# Duas coisas podem ser feitas para a estrutura de repetição:
# 1- Criar uma variável e atribuir o valor True
# 2- Ou criar todas as variáveis pedindo o código do cliente, altura e peso antes do laço e inclui-las dentro do
#    laço novamente até que finalize o programa.
# Neste caso, vamos criar a variável com o valor True
codigo = True

# Criando o laço:
# "Enquanto variável codigo for diferente de 0 faça"
while codigo != 0:
    # Variável n_cliente tem valor 1, sinalizando que o primeiro cliente colocará seus dados
    print('\nCliente nº:',n_cliente)
    # Variável código recebendo novo valor
    codigo = int(input("Digite o seu código: "))

    # Se a variável codigo for igual a 0, pare o programa.
    if codigo == 0:
        break

    # Senão
    else:
        # As variáveis abaixo recebem valores com ponto flutuante.
        altura = float(input('Digite sua altura: '))
        peso = float(input('Digite seu peso: '))

        # Enviando dados para as listas
        cod_clientes.append(codigo)
        altura_clientes.append(altura)
        peso_clientes.append(peso)

        # Atribuindo novo valor ao n_cliente, somando +1 ao valor original
        n_cliente += 1

# Realizando senso. Buscará dentro da lista os menores valores e os maiores valores dentro dos índices.
cod_magro = peso_clientes.index(min(peso_clientes))
cod_gordo = peso_clientes.index(max(peso_clientes))
cod_alto = altura_clientes.index(min(altura_clientes))
cod_baixo = altura_clientes.index(max(altura_clientes))

# Gerando espaço entre as mensagens iniciais e os prints finais.
print ('\n' * 3)

print("Código do mais magro:",cod_clientes[cod_magro])
print("Código do mais gordo:",cod_clientes[cod_gordo])
print("Código do mais alto:",cod_clientes[cod_alto])
print("Código do mais baixo:",cod_clientes[cod_baixo])

# Sobre a média de peso e altura, mais uma vez duas formas
# 1- Pode-se calcular dentro do print
# 2- Pode-se calcular fora do print, neste caso será necessário criar novas variáveis para fazer isso.
# Mas vamos fazer o calculo das médias dentro do print. E vimos uma dízima.

med_altura = sum(altura_clientes)/ len(altura_clientes)
med_peso = sum(peso_clientes)/ len(peso_clientes)

# o sum(altura_clientes) quer dizer: "Some todos os valores dentro da lista", e o len(altura_clientes): "Mostre o total de índices da lista"
# Quando usamos o '%.2f' significa que o valor só terá 2 casa decimais. Assim limita-se a dois números após o ponto da dízima.
print("A média de altura é: %.2fm"%med_altura)
print("A média de peso é:%.2fKg"%med_peso)