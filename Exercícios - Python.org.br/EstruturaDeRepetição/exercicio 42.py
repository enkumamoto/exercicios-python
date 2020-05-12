'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''
list1 = []
list2 = []
list3 = []
list4 = []

for n in range(100, -20, -1):
    if n > 75:
        list1.append(n)
    elif n >50 and n <=75:
        list2.append(n)
    elif n >25 and n <=50:
        list3.append(n)
    elif n > -1 and n <= 25:
        list4.append(n)
    else:
        break



print (list1)
print (list2)
print (list3)
print (list4)

