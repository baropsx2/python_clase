# Crear una función que reciba una lista y un número, quitar el núnero todas las veces de la lista.


numbers = [2, 7, 5, 8, 9, 8, 3, 7, 7]

'''
def erase_number(lista, num):
    d = {}
    for i in lista:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)

    d2 = d.copy()

    for k, v in d.items():
        if k == num:
            key = k
            del d2[key]
    print(d2)
    return d2


erase_number(numbers, 7)
'''

def erase_numbers(lista, num):
    resultado = []
    for i in lista:
        if i != num:
            resultado.append(i)
    print(resultado)
    return resultado
