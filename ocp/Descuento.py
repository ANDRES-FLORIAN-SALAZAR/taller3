from abc import ABC, abstractmethod


# Interfaz para los descuentos (OCP)
class Descuento(ABC):
    @abstractmethod
    def aplicar_descuento(self, precio):
        pass

# Descuento regular 
class DescuentoRegular(Descuento):
    def aplicar_descuento(self, precio):
        return precio * 0.9

# Descuento VIP
class DescuentoVIP(Descuento):
    def aplicar_descuento(self, precio):
        return precio * 0.8

# Descuento Black Friday
class BlackFridayDescuento(Descuento):
    def aplicar_descuento(self, precio):
        return precio * 0.3