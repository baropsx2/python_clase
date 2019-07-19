'''
Crear una funcion que recorra una lista y que multiplique todos sus valores por un valor dado

ejemplo:
por_n([1, 2, 3, 4], 2) ---> [2, 4, 6, 8]
por_n([1, 2, 3], 5)  --->  [5, 10, 15]
por_n([2, 3, 4, 5], 6)  -->  [12, 18, 24, 30]
'''


def por_n(lista, v):
    resultado = []
    for elem in lista:
        resultado.append(elem * v)
    print(resultado)
    return resultado


por_n([1, 2, 3, 4], 2)
por_n([1, 2, 3], 5)
por_n([2, 3, 4, 5], 6)
