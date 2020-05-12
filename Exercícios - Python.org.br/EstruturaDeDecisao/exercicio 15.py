'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
'''
def triangulo():
    if tri > ld3:
        try:
            if ld1 == ld2 == ld3:
                return "Triângulo Equilátero"

            elif ld1 == ld2 or ld2 == ld3 or ld3 == ld1:
                return "Triângulo Isósceles"

            else:
                return "Triângulo Escaleno"

        except:
            return 'Dados inválidos'

print('Qual o é o triângulo?')

ld1 = int(input('Digite o valor do primeiro lado em cm: '))
ld2 = int(input('Digite o valor do segundo lado em cm: '))
ld3 = int(input('Digite o valor do terceiro lado em cm: '))

tri = ld1 + ld2

print(triangulo())