def stock_bajo(inventario, limite):
    return [nombre for nombre, datos in inventario.items() if datos["cantidad"] < limite]

def valor_total(inventario):
    return sum(datos["precio"] * datos["cantidad"] for nombre, datos in inventario.items())

def nombres_en_mayuscula(inventario):
    return sorted([nombre.upper() for nombre in inventario.keys()])
