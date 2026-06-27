class Nodo:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mapa = {} # Mapea KEY -> Objeto NODO O(1)
        # Crear nodo Centinela (Lista circular vacía)
        self.root = Nodo()
        self.root.prev = self.root
        self.root.next = self.root
        #capacity
        self.capacity= capacity
    def remove(self, nodo):
        nodo.prev.next = nodo.next
        nodo.next.prev = nodo.prev

    def append(self, nodo):
        ultimo = self.root.prev
        nodo.prev = ultimo
        nodo.next = self.root
        ultimo.next = nodo
        self.root.prev = nodo
    
    def get(self, key: int) -> int:
        if key in self.mapa:
            nodo = self.mapa[key]
            self.remove(nodo)
            self.append(nodo)
            return nodo.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # SI LA LLAVE YA EXISTE: Extraer el nodo en O(1)
        if key in self.mapa:
            nodo = self.mapa[key]
            nodo.val = value # Actualizar valor
            
            # Desconectar de su posición actual en el medio
            self.remove(nodo)
        else:
            # SI ES NUEVA: Crear nodo físico 
            nodo = Nodo(key, value)
            self.mapa[key] = nodo
            if len(self.mapa) > self.capacity:
                # necesito eliminar el primero
                antiguo_primero = self.root.next
                self.mapa.pop(antiguo_primero.key, "no encontrado")
                self.remove(antiguo_primero)
            

        # INSERTAR AL FINAL SIEMPRE (Tanto para nuevos como actualizados)
        self.append(nodo)
