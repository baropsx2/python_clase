def suma_todos(l = []):
    result = 0
    for elem in l:
        result += elem
    return result


print(suma_todos())
print(suma_todos)
print(suma_todos([]))
print(suma_todos([1, 2, 3]))
# print(suma_todos(['A', 'B', 'C']))
print(suma_todos.__name__)
