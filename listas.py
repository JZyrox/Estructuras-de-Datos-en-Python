class Lista:
    def __init__(self):  # ← Aquí está la corrección
        """Inicializa una lista vacía."""
        self.elementos = []

    def agregar(self, elemento):
        """Agrega un elemento al final de la lista."""
        self.elementos.append(elemento)
        print(f"Agregado: {elemento}")

    def eliminar(self, elemento):
        """Elimina el primer elemento que coincida si existe."""
        if elemento in self.elementos:
            self.elementos.remove(elemento)
            print(f"Eliminado: {elemento}")
        else:
            print(f"No se encontró el elemento: {elemento}")

    def mostrar(self):
        """Devuelve la lista de elementos."""
        print("Contenido de la lista:", self.elementos)
        return self.elementos

    def esta_vacia(self):
        """Retorna True si la lista está vacía."""
        return len(self.elementos) == 0

    def tamaño(self):
        """Retorna el número de elementos en la lista."""
        return len(self.elementos)

    def buscar(self, elemento):
        """Retorna True si el elemento está en la lista."""
        encontrado = elemento in self.elementos
        print(f"Buscar '{elemento}': {'Encontrado' if encontrado else 'No encontrado'}")
        return encontrado


# Ejemplo de uso
lista = Lista()
lista.agregar(10)
lista.agregar(20)
lista.mostrar()             # [10, 20]
lista.buscar(10)            # Encontrado
lista.eliminar(10)
lista.eliminar(30)          # No se encontró
lista.mostrar()             # [20]
print("Tamaño:", lista.tamaño())
print("¿Está vacía?", lista.esta_vacia())
