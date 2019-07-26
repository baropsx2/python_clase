# La función debe recibir 3 números y debe devolver true si la multiplicación de los primeros dos es submúltiplo del tercero

""" Solución 1
def mult_submult(n1, n2, n3):
    mult = n1 * n2
    x = mult % n3 == 0
    print(x)
    return x


mult_submult(2, 4, 8)
"""
# Solución 2


def mult_submult(n1, n2, n3):
    mult = n1 * n2
    if mult % n3 == 0:
        print(True)
        return True
    else:
        print(False)
        return False


mult_submult(2, 4, 9)