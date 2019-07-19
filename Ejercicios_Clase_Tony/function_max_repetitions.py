# Hacer una función que reciba una lista y que devuelva el elemento con el menor número de ocurrencias


def max_repet(lista):
    dicc = {}
    for i in lista:
        if i in dicc:
            dicc[i] += 1
        else:
            dicc[i] = 1
    print(dicc)

    coinc = None
    total = 0
    for k, v in dicc.items():
        if v > total:
            total = v
            coinc = k
    print(coinc)
    return coinc


max_repet(nums)
