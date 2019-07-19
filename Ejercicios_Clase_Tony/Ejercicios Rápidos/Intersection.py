"""
Crear una función que se llame match_dicc, esta va a recibir 2 diccionarios, d1 y d2, y va a devolver un diccionario con
 la intersección de los dos diccionarios
"""


def match_dicc(d1, d2):
    resultado = {}
    for key, val in d1.items():
        for key2, val2 in d2.items():
            if key == key2 and val == val2:
                resultado.update({key: val})
    print(resultado)
    return resultado


d1 = {
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 8
}

d2 = {
    9: 10,
    8: 9,
    7: 8,
    6: 7,
    5: 6
}

match_dicc(d1, d2)
