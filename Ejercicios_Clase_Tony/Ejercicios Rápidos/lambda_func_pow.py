# Crear una expresión lambda que devuelva una funcion,
# la función que devuelva debe recibir un parámetro y elevarlo a la X potencia (X es definido en la primera expresión)


f_pow = lambda x: lambda y: x ** y
# y
f2 = f_pow(4)
# x
print(f2(6))

