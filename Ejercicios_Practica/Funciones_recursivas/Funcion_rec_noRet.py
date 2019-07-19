def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("Booooooom!")
    print("Fin de la función", numero)


print(cuenta_regresiva(10))
