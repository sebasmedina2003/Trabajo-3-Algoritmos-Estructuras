from categoria import Categoria

class Nodo:
    def __init__(self, valor:Categoria) -> None:
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.profundidad = None

class ArbolBinario:
    """
    No me pregunten como funciona att: Sebastian
    """
    def __init__(self) -> None:
        self.raiz = None
    
    def insertar(self, categoria:Categoria):
        if self.raiz is None:
            self.raiz = Nodo(categoria)
        else:
            self._insertar_recursivo(categoria, self.raiz)
        
    def _insertar_recursivo(self, categoria:Categoria, nodoActual:Nodo):
        if nodoActual.izquierda is None and nodoActual.derecha is None:
            nodoActual.izquierda = Nodo(categoria)

        elif nodoActual.izquierda is not None and nodoActual.derecha is None:
            nodoActual.derecha = Nodo(categoria)
            
        elif nodoActual.izquierda is not None and nodoActual.derecha is not None:
            try:
                if nodoActual.izquierda.izquierda is None:
                    self._insertar_recursivo(categoria, nodoActual.izquierda)
                elif nodoActual.izquierda.derecha is None:
                    self._insertar_recursivo(categoria, nodoActual.izquierda)
                elif nodoActual.derecha.izquierda is None:
                    self._insertar_recursivo(categoria, nodoActual.derecha)
                else:
                    self._insertar_recursivo(categoria, nodoActual.derecha)
            except:
                self._insertar_recursivo(categoria, nodoActual.izquierda)
    
    def eliminar(self, categoria:Categoria):
        self._eliminarRecursivo(categoria, self.raiz)
    
    def _eliminarRecursivo(self, categoria:Categoria, nodoActucal:Nodo):
        if nodoActucal is None:
            return None
        elif nodoActucal.izquierda.valor == categoria:
            nodoActucal.izquierda = None
            return None
        elif nodoActucal.derecha.valor == categoria:
            nodoActucal.derecha = None
            return None
        else:
            try:
                self._eliminarRecursivo(categoria, nodoActucal.derecha)
                self._eliminarRecursivo(categoria, nodoActucal.izquierda)
            except:
                return None
            
    def preOrder(self):
        self._preOrder(self.raiz)
    
    def _preOrder(self, nodoActual:Nodo):
        if nodoActual is not None:
            print(f"Nodo Actual: {nodoActual.valor},   Nodo Izquierdo: {nodoActual.izquierda.valor if nodoActual.izquierda is not None else 'Sin nodos'}  Nodo Derecho: {nodoActual.derecha.valor if nodoActual.derecha is not None else 'Sin nodos'}")
            self._preOrder(nodoActual.izquierda)
            self._preOrder(nodoActual.derecha)

"""
Prueba del arbol binario
"""

arbol = ArbolBinario()
arbol.insertar(1)
arbol.insertar(2)
arbol.insertar(3)
arbol.insertar(4)
arbol.insertar(5)
arbol.insertar(6)
arbol.insertar(7)
arbol.insertar(8)
arbol.insertar(9)
arbol.insertar(10)
arbol.preOrder()
print("\nEliminando el valor 3\n")
arbol.eliminar(3)
arbol.preOrder()