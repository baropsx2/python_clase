def factorial(numero):
    print("Valor inicial ->", numero)
    if numero > 1:
        numero = numero * factorial(numero -1)
    print("Valor final ->", numero)
    return numero


print(factorial(5))