def multiplica_por_5():
    while True:
        valor = (yield) * 5
        yield valor


m = multiplica_por_5()
next(m)
print(m.send(10))
print(m.send(3))
print(m.send(2))
