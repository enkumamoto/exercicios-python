'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
print ('Pintada na parede!')
tamanho_da_area = float(input('Nos informe o tamanho da área em m²: '))

preco_lata_tinta = 80
metro_por_litro = 3

total_de_latas = (tamanho_da_area * metro_por_litro) / 18
total_a_pagar = total_de_latas * preco_lata_tinta

if total_de_latas < 1:
    print(f'Para a área de {tamanho_da_area}m²\nserá necessário uma lata de tinta.\nTotal a pagar: R${preco_lata_tinta}')
else:
    print(f'Para a área de {tamanho_da_area}m²')
    print ('serão necessárias %.f latas de tinta.'%total_de_latas)
    print('Total a pagar: R$%.2f'%total_a_pagar)