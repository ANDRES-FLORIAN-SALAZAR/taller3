from ocp.Descuento import Descuento

# Clase que calcula el precio final con el descuento aplicado
class CalculadoraDescuentos:
    def __init__(self, descuento: Descuento):
        self.descuento = descuento

    def calcular_precio_final(self, precio):
        return self.descuento.aplicar_descuento(precio)