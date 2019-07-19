# 1. Hacer una función que reciba una lista y que devuelva el elemento con el menor número de ocurrencias
# l= [1, 1, 1, 2, 2, 1, 1, 1]          devuelve 2     porque solo aparece 2 veces


nums = [1, 1, 1, 2, 2, 1, 1, 1]


def min_repet(lista):
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
        if v < total or total == 0:
            total = v
            coinc = k
    print(coinc)
    return coinc


min_repet(nums)
