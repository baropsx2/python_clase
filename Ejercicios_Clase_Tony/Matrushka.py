def matrushka(lista):
    if type(lista) == type([]):
        lista_matrushka = matrushka(lista[0])
        return lista_matrushka

    print(lista)
    return lista


matrushka([[[[[5]]]]])
