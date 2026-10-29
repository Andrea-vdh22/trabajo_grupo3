def agregar_producto(inventario, nombre, precio, cantidad):
    if nombre in inventario:
        inventario[nombre]["cantidad"] += cantidad
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

def listar_productos(inventario):
    for nombre, datos in inventario.items():
        print(f"Producto: {nombre} | Precio: {datos['precio']} | Cantidad: {datos['cantidad']}")