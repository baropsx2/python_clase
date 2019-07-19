class nodo:
    def __init__(self, v):
        self.val = v
        self.izq = None
        self.der = None

    def inserta(self, n):
        raiz_actual = None
        if n.val < self.val:
            if self.izq == None:
                self.izq = n
            else:
                raiz_actual.inserta(n)
        elif n.val > self.val:
            if self.der == None:
                self.der = n
            else:
                raiz_actual.inserta(n)
        else:
            return None


r = nodo(20)
h = nodo(11)
r.inserta(h)
print(r.val)

h = nodo(15)
r.inserta(h)
print(r.val)

h = nodo(28)
r.inserta(h)
print(r.val)

h = nodo(26)
r.inserta(h)
print(r.val)

h = nodo(27)
r.inserta(h)
print(r.val)

h = nodo(27.5)
r.inserta(h)
print(r.val)

h = nodo(11)
r.inserta(h)
print(r.val)
