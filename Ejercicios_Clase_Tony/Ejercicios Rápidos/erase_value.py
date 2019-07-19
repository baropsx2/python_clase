'''
Crear una función que reciba un diccionario como argumento y un valor, lo que vas a hacer es devolver un diccionario que
sea igual al otro, pero que no tenga la pareja de datos cuyo valor sea igual al valor dado
'''


def erase_value(dicc, val_elim):
    d1 = {}
    for k, v in dicc.items():
        if v != val_elim:
            d1.update({k: v})

    print(d1)
    return d1


d = {
    "hola": 1,
    "mundo": 256,
    2: "frfr"
}


erase_value(d, "frfr")
erase_value(d, 1)
erase_value(d, 2)
