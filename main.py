import inventario
import reportes

def main():
    # 1. Crear el diccionario inicial con los datos base
    inventario_actual = {}
    
    # 2. Ciclo while para mantener el menú activo hasta que se elija Salir
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Listar productos")
        print("4. Ver productos con stock bajo")
        print("5. Ver valor total")
        print("6. Ver nombres en mayúscula")
        print("7. Salir")
        
        opcion = input("Selecciona una opción (1-7): ")
        
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break # Rompe el ciclo while para terminar el programa
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()