'''
Faça um programa que mostre os n termos da Série a seguir:

      S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

    Imprima no final a soma da série.
'''
dividendo = 1
divisor = 1
dvd = []
dvs = []

limite = int(input('Digite um limite para o dividendo:'))


while dividendo <= limite -1:
    print(f'{dividendo}/{divisor} + ',end='')
    dvd.append(dividendo)
    dvs.append(divisor)
    dividendo += 1
    divisor += 2

print(dividendo,'/',divisor,'=',sum(dvd),'/', sum(dvs))
