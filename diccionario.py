class Diccionario:
    def __init__(self, size=10):  # Corregido
        self.size = size
        self.tabla = [[] for _ in range(size)]

    def _hash(self, clave):
        """Calcula el índice usando la función hash de Python y módulo del tamaño."""
        indice = hash(clave) % self.size
        print(f"Hash de '{clave}' → índice {indice}")
        return indice

    def agregar(self, clave, valor):
        indice = self._hash(clave)
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                self.tabla[indice][i] = (clave, valor)
                print(f"Actualizado: ({clave}: {valor}) en índice {indice}")
                return
        self.tabla[indice].append((clave, valor))
        print(f"Agregado: ({clave}: {valor}) en índice {indice}")

    def obtener(self, clave):
        indice = self._hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                print(f"Obtenido: {clave} → {v}")
                return v
        print(f"Clave '{clave}' no encontrada.")
        return None

    def eliminar(self, clave):
        indice = self._hash(clave)
        for i, (k, _) in enumerate(self.tabla[indice]):
            if k == clave:
                del self.tabla[indice][i]
                print(f"Eliminado: {clave} del índice {indice}")
                return
        print(f"Clave '{clave}' no encontrada. No se pudo eliminar.")

    def mostrar_tabla(self):
        print("\nTabla Hash:")
        for i, lista in enumerate(self.tabla):
            print(f"[{i}] {lista}")


# --- Programa interactivo ---
if __name__ == "__main__":  # Corregido
    dic = Diccionario()

    while True:
        print("\nOpciones:")
        print("1. Agregar clave-valor")
        print("2. Obtener valor por clave")
        print("3. Eliminar clave")
        print("4. Mostrar tabla hash")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            clave = input("Ingrese la clave: ")
            valor = input("Ingrese el valor: ")
            dic.agregar(clave, valor)
        elif opcion == "2":
            clave = input("Ingrese la clave a buscar: ")
            dic.obtener(clave)
        elif opcion == "3":
            clave = input("Ingrese la clave a eliminar: ")
            dic.eliminar(clave)
        elif opcion == "4":
            dic.mostrar_tabla()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
