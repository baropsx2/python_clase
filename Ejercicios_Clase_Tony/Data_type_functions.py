# Ejercicio incompleto
def f1(a, b):
    return a + b
def f2(a, b):
    return a - b
def f3(a, b):
    if type(a) in [type(()), type([]), type({})]:
        return a[b]
    else:
        return None


d = {
    "s": f1,
    "r": f2,
    "gv": f3
}


print(d["s"](2, 3))
print(d["r"](2, -2))
print(d["gv"]([2, 3, "frfr"], -1))

s = d["gv"](d, "s")
print(s(1, -1))
