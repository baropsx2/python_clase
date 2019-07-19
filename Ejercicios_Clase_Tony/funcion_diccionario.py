def joven(diccionario):
    resultado = []
    for k, v in diccionario.items():
        if v < 30:
            resultado.append(k)
    print(resultado)
    return resultado


d = {
    "Tony": 32,
    "X": 26,
    "Y": 40,
}

joven(d)
