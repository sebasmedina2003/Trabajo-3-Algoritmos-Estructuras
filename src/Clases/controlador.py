from Clases.arbolCategoria import ArbolBinario

def menuControlador():
  print("\n+ ===== Menu controlador del sistema ===== +")
  print("|  1. Cargar los datos de categorias       |")
  print("|  2. Guardar los datos de categorías      |")
  print("|  3. Agregar categoría                    |")
  print("|  4. Eliminar categoría                   |")
  print("|  5. Buscar productos por categoría       |")
  print("|  6. Salir al menu principal              |")
  print("+ ======================================== +")

  while True:
    try: 
        opcion = int(input("=> Sección a trabajar: "))
        if opcion in range(1, 7):
            break
        else:
            print("\n>>> Valor fuera de las opciones...\n")
    except: 
        print("\n>>> Ingresar datos necesarios...\n")
  
  # Opciones de ingreso
  if opcion == 1:
    pass
  elif opcion == 2:
    pass
  elif opcion == 3:
     pass
  elif opcion == 4:
     pass
  elif opcion == 5:
     pass
  else:
     print("\n>>> De regreso al menu principal...\n")
     

class Controlador:
  def __init__(self, arbolBinario):
    # Arbol binario como atributo de la clase
    self.arbol = arbolBinario 

  def cargarDatos(self):
    pass

  def guardarDatos(self):
    pass

  def agregarCategoria(self):
    pass

  def eliminarCategoria(self):
    pass

# Instancia del controlador
arbol = None # Capturar el arbol del main
controlador = Controlador(arbol)