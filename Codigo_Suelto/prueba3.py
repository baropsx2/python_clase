def agrega_pais(dic_codigos, pais, codigo):
    pais_key = []
    codigo_val = []
    dicExtra = {}
    for key, val in dic_codigos.items():
        if key == pais:
            pais_key.append(key)
        elif val == codigo:
            codigo_val.append(val)
        else:
            pais_key.append(key), codigo_val.append(val)

    dicExtra = dict(zip(pais_key, codigo_val))
    dicExtra.update(dic_codigos)
    print(dic_codigos)
    return dic_codigos


codigos = {"Albania": 355,
           "Alemania": 49,
           "Mexico": 52
           }


agrega_pais(codigos, "USA", 1)
agrega_pais(codigos, "Mexico", 54)

# dict(pais, codigos) = dicExtra
# if dicExtra.items() == codigos.items():
# codigos.update(dicExtra)
