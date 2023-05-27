# Importar clases 
from Clases.categoria import Categoria

# Menu principal
def menu():
    print("+ =========: Menú principal :========== +")
    print("| 1. Cargar categorías desde archivo    |")
    print("| 2. Agregar una nueva categoría        |")
    print("| 3. Elimnar categoría                  |")
    print("| 4. Buscar productos por categoría     |")
    print("| 5. Gestionar categorías de productos  |")
    print("+ ===================================== +\n")
    
    while True:
        try: 
            opcion = int(input("=> Sección a trabajar: "))
            if opcion in range(1, 6):
                break
            else:
                print("\n>>> Valor fuera de las opciones...\n")
        except: 
            print("\n>>> Ingresar datos necesarios...\n")

# Correr la funcion principal
if __name__ == "__main__":
    menu()