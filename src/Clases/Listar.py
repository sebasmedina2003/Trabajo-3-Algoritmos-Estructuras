
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_aux(nuevo_nodo, self.raiz)

    def _insertar_aux(self, nuevo_nodo, nodo_actual):
        if nuevo_nodo.valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._insertar_aux(nuevo_nodo, nodo_actual.izquierdo)
        elif nuevo_nodo.valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
               self._insertar_aux(nuevo_nodo, nodo_actual.derecho)

    def preorden(self):
        self._preorden_recursivo(self.raiz)

    def _preorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor, end=" ")
            self._preorden_recursivo(nodo_actual.izquierdo)
            self._preorden_recursivo(nodo_actual.derecho)

    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._inorden_recursivo(nodo_actual.izquierdo)
            print(nodo_actual.valor, end=" ")
            self._inorden_recursivo(nodo_actual.derecho)

    def postorden(self):
        self._postorden_recursivo(self.raiz)

    def _postorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._postorden_recursivo(nodo_actual.izquierdo)
            self._postorden_recursivo(nodo_actual.derecho)
            print(nodo_actual.valor, end=" ")

    
arbol = ArbolBinario()
arbol.insertar("Categorías")
arbol.insertar("Electrónica")
arbol.insertar("Moda")
arbol.insertar("Computadores")
arbol.insertar("Teléfonos")
arbol.insertar("Ropa")
arbol.insertar("Accesorios")
arbol.insertar("Portátiles")
arbol.insertar("Escritorio")
arbol.insertar("Móviles")

print("Recorrido en Preorden: \n·",end ="") # Categorías con nombres y descripción de los productos
arbol.preorden()
print("\nRecorrido en Inorden: \n·",end ="") # Estructura jerarquica de las categorías 
arbol.inorden()
print("\nRecorrido en Postorden: \n·",end ="") #Categorías y subcategorías con sus cantidades
arbol.postorden()
