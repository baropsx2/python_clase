def get_pais(let_inic):
    paises = list()
    for key in codigos.keys():
        if key.startswith(let_inic):
            paises.append(key)

    print(paises)
    return paises


codigos = {"Albania": 355,
           "Alemania": 49,
           "Mexico": 52
           }

get_pais("A")
get_pais("M")
