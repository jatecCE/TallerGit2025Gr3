# test_inventario_productos.py
#Instalr pytest y unittest
import unittest
from InventarioProductos import InventarioProductos  

class TestInventarioProductos(unittest.TestCase): # la clase hereda de unittest.TestCase

    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.inv = InventarioProductos()
        self.inv.agregar_producto("A1", "Teclado", 50.0, 10)
        self.inv.agregar_producto("B2", "Mouse", 25.0, 5)


    def test_agregar_producto_correcto(self):
        resultado = self.inv.agregar_producto("C3", "Monitor", 120.0, 3)
        self.assertIsInstance(resultado, dict)
        self.assertEqual(resultado["codigo"], "C30")
        self.assertIn("C3", self.inv.productos)


    def test_agregar_producto_codigo_existente(self):
        resultado = self.inv.agregar_producto("A1", "Otro", 10.0, 1)
        self.assertEqual(resultado, "Codigo existente")


    def test_agregar_producto_precio_invalido(self):
        resultado = self.inv.agregar_producto("D4", "Impresora", -15.0, 2)
        self.assertEqual(resultado, "Precio invalido")


    def test_agregar_producto_cantidad_invalida(self):
        resultado = self.inv.agregar_producto("E5", "Laptop", 800.0, -1)
        self.assertEqual(resultado, "Cantidad invalida")


    
    def test_vender_producto_correctamente(self):
        cantidad_restante = self.inv.vender_producto("A1", 3)
        self.assertEqual(cantidad_restante, 7)
        self.assertEqual(self.inv.productos["A1"]["cantidad"], 7)

    def test_vender_producto_inexistente(self):
        resultado = self.inv.vender_producto("Z9", 1)
        self.assertEqual(resultado, "Producto inexistente")

    def test_vender_producto_cantidad_invalida(self):
        resultado = self.inv.vender_producto("A1", -2)
        self.assertEqual(resultado, "cantidad invalida")

    def test_vender_producto_stock_insuficiente(self):
        resultado = self.inv.vender_producto("B2", 10)
        self.assertEqual(resultado, "cantidad insuficiente")


   
    def test_reabastecer_producto_correctamente(self):
        nuevo_stock = self.inv.reabastecer_producto("A1", 5)
        self.assertEqual(nuevo_stock, 15)

    def test_reabastecer_producto_inexistente(self):
        resultado = self.inv.reabastecer_producto("Z1", 5)
        self.assertEqual(resultado, "Producto inexistente")

    def test_reabastecer_cantidad_invalida(self):
        resultado = self.inv.reabastecer_producto("A1", 0)
        self.assertEqual(resultado, "cantidad invalida")

  
    def test_valor_total_inventario(self):
        esperado = (50.0 * 10) + (25.0 * 5)
        self.assertEqual(self.inv.valor_total_inventario(), esperado)

  
    def test_buscar_producto_existente(self):
        resultado = self.inv.buscar_producto("mouse")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["nombre"], "Mouse")

    def test_buscar_producto_inexistente(self):
        resultado = self.inv.buscar_producto("pantalla")
        self.assertEqual(resultado, [])

  
    def test_obtener_producto_existente(self):
        producto = self.inv.obtener_producto("A1")
        self.assertEqual(producto["nombre"], "Teclado")

    def test_obtener_producto_inexistente(self):
        resultado = self.inv.obtener_producto("Z5")
        self.assertEqual(resultado, "Producto inexistente")


    def test_lista_productos(self):
        lista = self.inv.lista_productos()
        self.assertIsInstance(lista, list)
        self.assertEqual(len(lista), 2)
        self.assertTrue(any(p["codigo"] == "A1" for p in lista))

if __name__ == "__main__":
    unittest.main()
    
    
"""Tipos de assertions comunes:

- assertEqual(a, b): Verifica que a y b sean iguales.
- assertNotEqual(a, b): Verifica que a y b no sean iguales. 
- assertTrue(x): Verifica que x sea True.
- assertFalse(x): Verifica que x sea False.
- assertIs(a, b): Verifica que a y b sean el mismo objeto.
- assertIsNot(a, b): Verifica que a y b no sean el mismo objeto.
- assertIsNone(x): Verifica que x sea None.
- assertIsNotNone(x): Verifica que x no sea None.
- assertIn(a, b): Verifica que a esté en b.
- assertNotIn(a, b): Verifica que a no esté en b.
- assertIsInstance(a, b): Verifica que a sea instancia de b.
- assertNotIsInstance(a, b): Verifica que a no sea instancia de b.
-assertRaises(Exception, func, *args): Verifica que al llamar a func con args se lance la excepción Exception.

"""