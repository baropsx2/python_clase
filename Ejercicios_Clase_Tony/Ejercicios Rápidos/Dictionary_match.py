# Jul/22/2019
# Función - Recibir una lista y un diccionario como parámetro, y como resultado debe devolver todos los valores del
# del diccionario en una que hagan match con los elementos de la lista en


def match_ld(lista, dicc):
    matched = []
    for k, v in dicc.items():
        if k in lista:
            matched.append(v)
    print(matched)
    return matched


lista = [1, 2, 3, 4, 5]
dicc = {
    1: "one",
    2: "two",
    3: "three",
    7: "seven",
    5: "five",
    6: "six"
}
match_ld(lista, dicc)
