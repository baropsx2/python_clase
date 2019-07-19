def del_n_v(lista, num, veces):
    list = []
    contador = 0
    indice = 0
    longitud = 0
    for k, i in enumerate(lista):
        if i != num:
            list.append(i)
        elif contador < veces:
            contador += 1
        else:
            indice = k
            longitud = len(lista)
            break
    return list + lista[indice:longitud]


l = [1, 2, 3, 4, 5, 6, 7, 10, 8, 9, 7, 10, 10, 8, 6, 5, 10]
print(del_n_v(l, 10, 3))

