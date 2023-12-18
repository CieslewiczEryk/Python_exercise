print("Sortowanie babelkowe")

lista = [2,0,5,1,6,3]
n = len(lista)
# print(n)
'''
lista[0], lista[1] = lista[1], lista[0]

print(lista)
'''

for number in lista:
    for pos in range(len(lista)-1):
    #    print(pos)
        if lista[pos] > lista[pos + 1]:
            lista[pos], lista[pos + 1] = lista[pos + 1], lista[pos]
            print(lista)
        else:
            continue
print(lista)
