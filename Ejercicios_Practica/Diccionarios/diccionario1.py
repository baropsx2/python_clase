currencies = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}


currency = input("Introduce una divisa: ")
print(currencies.get(currency.title(), "La divisa no está en el diccionario."))
