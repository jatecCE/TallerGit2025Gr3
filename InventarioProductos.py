class InventarioProductos:
    def __init__(self):
        """
        La estructura del diccionario de productos es:
        {
            "codigo": str,
            "nombre": str,
            "precio": float,
            "cantidad": int
        }
        """
        self.productos = {}

    def agregar_producto(self, codigo, nombre, precio, cantidad):
        
        if codigo in self.productos:
            return "Codigo existente"
        if precio <= 0:
            return "Precio invalido"
        if cantidad < 0:
            return "Cantidad invalida"

        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        self.productos[codigo] = producto
        return producto

    def vender_producto(self, codigo, cantidad):
        """
        Disminuye la cantidad de un producto al venderlo.
        Retorna la cantidad restante o un mensaje de error.
        """
        if codigo not in self.productos:
            return "Producto inexistente"
        if cantidad <= 0:
            return "cantidad invalida"
        
        producto = self.productos[codigo]
        if producto["cantidad"] < cantidad:
            return "cantidad insuficiente"

        producto["cantidad"] -= cantidad
        return producto["cantidad"]

    def reabastecer_producto(self, codigo, cantidad):
        """
        Aumenta la cantidad de un producto existente.
        Retorna el nuevo stock o un mensaje de error.
        """
        if codigo not in self.productos:
            return "Producto inexistente"
        if cantidad <= 0:
            return "cantidad invalida"

        producto = self.productos[codigo]
        producto["cantidad"] += cantidad
        return producto["cantidad"]

    def valor_total_inventario(self):
        """
        Retorna el valor  total del inventario.
        """
        total = 0
        for producto in self.productos.values():
            subtotal = producto["precio"] * producto["cantidad"]
            total += subtotal
        return total

    def buscar_producto(self, termino):
        """
        Busca productos cuyo nombre contenga el término .
        Devuelve lista de coincidencias.
        """
        coincidencias = []
        termino = termino.lower()

        for producto in self.productos.values():
            nombre = producto["nombre"].lower()
            if termino == nombre:
                coincidencias.append(producto)

        return coincidencias

    def obtener_producto(self, codigo):
        """
        Devuelve la información completa de un producto según su código.
        """
        if codigo in self.productos:
            return self.productos[codigo]
        else:
            return "Producto inexistente"

    def lista_productos(self):
        """
        Devuelve una lista con todos los productos.
        """
        lista = []
        for p in self.productos.values():
            lista.append(p)
        return lista
    
#inventario1= InventarioProductos()
#inventario1.agregar_producto("CE1", "Teclado", 50.0, 10)
#inventario1.agregar_producto("CE2", "Mouse", 25.0, 5)
#print(inventario1.valor_total_inventario())