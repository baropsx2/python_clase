'''
necesito las siguientes funciones:
get_codigo(dic_codigos, pais)    --->    Devuelve el codigo telefónico del país que recibe si existe, caso contrario devuelve un None
    ejemplo:   get_codigo(codigos, "Mexico")  --->   52
               get_codigo(codigos, "Albania")  ---->   355
               get_codigo(codigos, "USA")  --->   None

get_paises(dic_codigos)   --->    Devuelve una lista con los nombres de los países en el diccionario de codigos
                      get_paises(codigos)  --->  ["Albania", "Alemania", "Mexico"]

get_pais(letra)  --->  Devuelve una lista con los países que empiecen con la letra dada:
                      get_pais("A")   --->   ["Albania", "Alemania"]   tip: checa el método "startswith" de las cadenas
                      get_pais("M")  --->  ["Mexico"]

def agrega_pais(dic_codigos, pais, codigo)    --->   Agrega o actualiza el pais dado al diccionario de codigos
    agrega_pais(codigos, "USA", 1)    --->    Devuelve el diccionario codigos con la inserción de {"USA": 1}
    agrega_pais(codigos, "Mexico", 54)    --->    Devuelve el diccionario codigos con la actualización de {"Mexico": 54}
'''

# Función para devolver el código telefónico del país que recibe si existe, caso contrario devuelve None


def get_codigo(dic_codigos, pais):
    for key, val in dic_codigos.items():
        if key == pais:
            print(val)
            return val
    return None

# Devuelve una lista con los nombres de los países en el diccionario de codigos


def get_paises(dic_codigos):
    lista_paises = list()
    for key in dic_codigos.keys():
        lista_paises.append(key)
    print(lista_paises)
    return lista_paises

# Devuelve una lista con los países que empiecen con la letra dada:


def get_pais(let_inic):
    paises = list()
    for key in codigos.keys():
        if key.startswith(let_inic):
            paises.append(key)
    print(paises)
    return paises

# 4a función - Incompleta


def agrega_pais(dic_codigos, pais, codigo):
   # dic_codigos[pais] = codigo
    dic_codigos.update({pais: codigo})
    return dic_codigos


codigos = {"Albania": 355,
           "Alemania": 49,
           "Mexico": 52
           }


get_codigo(codigos, "Mexico")
get_codigo(codigos, "Albania")
get_codigo(codigos, "USA")

get_paises(codigos)

get_pais("A")
get_pais("M")

agrega_pais(codigos, "USA", 1)
agrega_pais(codigos, "Mexico", 54)
