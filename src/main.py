# Importar clases 
from Clases.categoria import Categoria
from Clases.controlador import menuControlador

# Menu principal
def menu():
    while True:
        print("+ =========: Menú principal :========== +")
        print("| 1. Cargar categorías desde archivo    |")
        print("| 2. Agregar una nueva categoría        |")
        print("| 3. Elimnar categoría                  |")
        print("| 4. Buscar productos por categoría     |")
        print("| 5. Gestionar categorías de productos  |")
        print("| 6. Acceder al controlador del sistema |")
        print("| 7. Salir del sistema                  |")
        print("+ ===================================== +\n")
        
        while True:
            try: 
                opcion = int(input("=> Sección a trabajar: "))
                if opcion in range(1, 8):
                    break
                else:
                    print("\n>>> Valor fuera de las opciones...\n")
            except: 
                print("\n>>> Ingresar datos necesarios...\n")
        
        # Acceder al menu de la opcion 
        if opcion == 1: # Carga categoria
            pass
        elif opcion == 2: # Agrega categoria
            pass
        elif opcion == 3: # Elimina categoria
            pass
        elif opcion == 4: # Busca por categoria
            pass
        elif opcion == 5: # Gestiona categorias
            pass
        elif opcion == 6: # Accede al controlador del sistema
            menuControlador() 
        else:
            print("\n>>> Ha salido del sistema...")
            break

# Correr la funcion principal
if __name__ == "__main__":
    menu()