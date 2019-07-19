def pares(l):
    m = []
    for n in l:
        if n % 2 == 0:
            m.append(n)
    print(m)
    return m


l = []
pares([1, 2, 3, 4])
pares([11, 12, 13])
print(pares)