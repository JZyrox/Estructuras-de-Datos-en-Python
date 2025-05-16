class Nodo:
    def __init__(self, valor):  # corregido __init__
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):  # corregido __init__
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar_rec(nodo.izq, valor)
        else:
            nodo.der = self._insertar_rec(nodo.der, valor)
        return nodo

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self.inorden(nodo.der)

    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izq)
            self.preorden(nodo.der)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.valor, end=" ")

# --- Programa interactivo ---
if __name__ == "__main__":  # corregido __name__ y __main__
    arbol = ArbolBinario()

    while True:
        print("\nOpciones:")
        print("1. Insertar nodo")
        print("2. Mostrar recorrido Inorden")
        print("3. Mostrar recorrido Preorden")
        print("4. Mostrar recorrido Postorden")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            valor = int(input("Ingrese el valor a insertar: "))
            arbol.insertar(valor)
        elif opcion == "2":
            print("Recorrido inorden:")
            arbol.inorden(arbol.raiz)
            print()
        elif opcion == "3":
            print("Recorrido preorden:")
            arbol.preorden(arbol.raiz)
            print()
        elif opcion == "4":
            print("Recorrido postorden:")
            arbol.postorden(arbol.raiz)
            print()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")
