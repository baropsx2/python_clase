'''
def multiplica_por_5():
    while True:
        valor = (yield) * 5
        yield valor


m = multiplica_por_5()
next(m)
print(m.send(10))
print(m.send(3))
print(m.send(2))
'''


def multiplica_por_n(n):
    while True:
        valor = (yield) * n
        yield valor


m = multiplica_por_n(5)
next(m)
print(m.send(10))
next(m)
print(m.send(2))

m2 = multiplica_por_n(2)
next(m2)
print(m2.send(10))
print(m2.send(2))

m3 = multiplica_por_n(3)
next(m3)
print(m3.send(5))
