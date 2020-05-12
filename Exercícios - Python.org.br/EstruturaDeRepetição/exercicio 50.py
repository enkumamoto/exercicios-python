'''
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
'''
limite = int(input('Digite o limite para o divisor: '))
h = 1
n = 2

n_list = []
h_list = []

print('H = 1 + ',end='')
while n <= limite - 1:
    print('',h,'/',n,' + ',end='')
    h_list.append(h)
    n_list.append(n)
    n += 1

print(h,'/',n,'=>',sum(h_list),'/',sum(n_list),'=>', round(sum(h_list)/sum(n_list)),2)