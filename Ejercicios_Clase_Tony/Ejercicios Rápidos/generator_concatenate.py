# Jul/22/2019
# Debe de recibir una cadena al inicializarlo y luego dentro del generador debe recibir otra cadena e imprimirla
# concatenando la cadena con la que lo inicializaste


def gen_concat(cadena):
    while True:
        conc_list = (yield) + cadena
        yield conc_list


cadena = gen_concat("World!")
next(cadena)
print(cadena.send("Hello "))


