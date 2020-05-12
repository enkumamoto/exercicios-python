'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número
de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''
pais_A = 80000
pais_B = 200000
year = 0

while pais_A <= pais_B:
    pais_A = pais_A + (pais_A * 0.03)
    pais_B = pais_B + (pais_B * 0.015)
    year += 1
    print('Relatório:\nAno: %a, Pop. País A: %.1f, Pop. País B: %.1f' % (year, pais_A, pais_B))

print('A população do País A ultrapassa ou igual do País B em %d anos.'%year)
