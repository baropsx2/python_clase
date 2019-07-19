def sumatoria(num):
    if num == 1:
        return 1
    else:
        return num + sumatoria(num - 1)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Insertar número para calcular la sumatoria: "))
print(sumatoria(num))

n = int(input("Insertar número para calcular el factorial: "))
print(factorial(n))
