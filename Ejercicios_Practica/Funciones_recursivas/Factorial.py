def factorial(numero):
    if numero == 0 or numero == 1:
       # print(1)
        return 1
    else:
        print(numero * factorial((numero - 1)))
        return numero * factorial(numero - 1)


factorial(7)
