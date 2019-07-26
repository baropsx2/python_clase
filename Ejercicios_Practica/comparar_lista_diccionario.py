def match_ld(lista, dicc):
    matched = []
    for values in dicc.values():
        if values in lista:
            matched.append(values)
    print(matched)
    return matched


lista = ["one", "two", "three", "four", "five", "eight"]
dicc = {
    1: "one",
    2: "two",
    3: "three",
    7: "seven",
    5: "five",
    6: "six"
}
match_ld(lista, dicc)