# Paso 1: Definir la estructura del Nodo
class Node:
    def __init__(self, data):  # Corregido: __init__
        self.data = data
        self.next = None

# Paso 2: Definir la estructura de la Lista Simplemente Enlazada
class SinglyLinkedList:
    def __init__(self):  # Corregido: __init__
        self.head = None

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current_node = self.head
        elements = []
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print("HEAD -> " + " -> ".join(elements) + " -> NULL")

# Paso 3: Usar la lista

my_list = SinglyLinkedList()

# Insertar 20 y luego 10
my_list.insert_at_beginning(20)
my_list.insert_at_beginning(10)

print("Lista inicial:")
my_list.print_list()
# HEAD -> 10 -> 20 -> NULL

# Insertar 5
print("\nInsertando 5 al principio...")
my_list.insert_at_beginning(5)

print("Lista después de la inserción:")
my_list.print_list()
# HEAD -> 5 -> 10 -> 20 -> NULL

# Insertar otro valor diferente al de tu compañero
my_list.insert_at_beginning(3)
my_list.print_list()
# HEAD -> 2 -> 5 -> 10 -> 20 -> NULL
