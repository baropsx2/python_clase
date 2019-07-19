diccionario = {
    'nombre' : 'Carlos',
    'edad' : 22,
    'cursos': ['Python','Django','JavaScript'],
    "":1
}


print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])
print(diccionario['cursos'][0])
print(diccionario['cursos'][1])
print(diccionario['cursos'][2])
print()
for key in diccionario:
    print(key, ":", diccionario[key])
