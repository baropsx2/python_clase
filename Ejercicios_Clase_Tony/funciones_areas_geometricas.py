def calcula_area(figura, argum):
    print(dicc)
    return dicc[figura](*argum)


def triangulo(base, altura):
    area = base * altura / 2
    return area


def cuadrado(base, altura):
    area = base * altura
    return area


def circulo(radio):
    pi = 3.1416
    area = pi * radio ** 2
    return area

dicc = {
    "triangulo": triangulo,
    "cuadrado": cuadrado,
    "circulo": circulo
}

calcula_area("cuadrado", [3, 4])
