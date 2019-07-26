def f(x):
    return 9

w = f
w(1)
print(w.__name__)
# print(dir(f))
# print(dir(w))

w = lambda x: 9 + x
print(w(1))
print(type(f))
print(type(w))
print(dir(w))
print(dir(f))
print(w.__name__)