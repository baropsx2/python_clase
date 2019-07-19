'''
Crear una función que se llame cadenas, la función va a recibir una lista y debe devolver una lista con las cadenas
que contenga la lista original.
Ejemplo:
cadenas([1, 2, 3, “hola”, 0, “mundo”]) ---> [“hola”, “mundo”]
cadenas([1, 2]) ---> []
cadenas([“hola”, 23, 56, “frfr”]) ---> [“hola”, “frfr”]
'''

def cadenas(lista):
    resultado = []
    for elem in lista:
        if type(elem) == type(""):
            resultado.append(elem)
        else:
            resultado
    print(resultado)
    return resultado


cadenas([1, 2, 3, "hola", 0, "mundo"])
cadenas([1, 2])
cadenas(["hola", 23, 56, "frfr"])
