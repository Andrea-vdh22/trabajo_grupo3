import inventario
import reportes

def main():
    # 1. Crear el diccionario inicial con los datos base
    inventario_actual = {}
    
    continuar = True

    while continuar == True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Listar productos")
        print("4. Ver productos con stock bajo")
        print("5. Ver valor total")
        print("6. Ver nombres en mayúscula")
        print("7. Salir")
        
        opcion = input("Selecciona una opción (1-7): ")
        
          # Pedimos los datos necesarios para agregar
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad en stock: "))
            inventario.agregar_producto(inventario_actual, nombre, precio, cantidad)
            
        elif opcion == "2":
            # Pedimos el nombre del producto a eliminar
            nombre = input("Nombre del producto que deseas eliminar: ")
            inventario.eliminar_producto(inventario_actual, nombre)
            
        elif opcion == "3":
            # Listamos todos los productos
            inventario.listar_productos(inventario_actual)
            
        elif opcion == "4":
            # Pedimos el límite para el reporte de stock bajo
            limite = int(input("Ingresa el límite de stock: "))
            productos_bajos = reportes.stock_bajo(inventario_actual, limite)
            print("Productos con stock bajo:", productos_bajos)
            
        elif opcion == "5":
            # Mostramos el valor total calculado
            total = reportes.valor_total(inventario_actual)
            print("El valor total del inventario es:", total)
            
        elif opcion == "6":
            # Mostramos los nombres en mayúscula ordenados
            nombres_mayus = reportes.nombres_en_mayuscula(inventario_actual)
            print("Nombres en mayúscula:", nombres_mayus)
            
        elif opcion == "7":
            print("Saliendo del programa...")
            continuar = False # Rompe el ciclo while
            
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()