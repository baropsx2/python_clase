def cuantos(cadena, caracter):
    ocurrencias = 0
    for x in cadena:
        if x == caracter:
            ocurrencias += 1
    print(ocurrencias)
    return ocurrencias


cuantos("hola mundo", "o")
cuantos("otra cosa", "a")
cuantos("fale frfr", "f")
cuantos("hola", "x")
