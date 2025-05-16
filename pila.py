class Pila:
    def __init__(self):  # Corregido
        self.elementos = []

    def apilar(self, elemento):
        print(f"Apilando: {elemento}")
        self.elementos.append(elemento)
        self.mostrar()

    def desapilar(self):
        if self.elementos:
            eliminado = self.elementos.pop()
            print(f"Desapilando: {eliminado}")
        else:
            print("La pila está vacía")
        self.mostrar()

    def mostrar(self):
        print("Estado de la pila:", self.elementos)


# COLA (FIFO)
from collections import deque

class Cola:
    def __init__(self):  # Corregido
        self.elementos = deque()

    def encolar(self, elemento):
        print(f"Encolando: {elemento}")
        self.elementos.append(elemento)
        self.mostrar()

    def desencolar(self):
        if self.elementos:
            eliminado = self.elementos.popleft()
            print(f"Desencolando: {eliminado}")
        else:
            print("La cola está vacía")
        self.mostrar()

    def mostrar(self):
        print("Estado de la cola:", list(self.elementos))


# DEMOSTRACIÓN
print("---- PILA ----")
pila = Pila()
pila.apilar("A")
pila.apilar("B")
pila.apilar("C")
pila.desapilar()
pila.desapilar()

print("\n---- COLA ----")
cola = Cola()
cola.encolar("1")
cola.encolar("2")
cola.encolar("3")
cola.desencolar()
cola.desencolar()
