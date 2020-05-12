'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
print('Vai dar tempo?')
print('Quer saber quanto tempo leva o seu download?')

tmn_arquivo = float(input('Nos informe o tamanho do arquivo em MB: '))
vel_link = int(input('Nos informe a velocidade do seu link de internet em Mbps: '))
tempo_down = (tmn_arquivo / vel_link) / 60
print('Seu arquivo será baixad em %.f minutos!'%tempo_down)