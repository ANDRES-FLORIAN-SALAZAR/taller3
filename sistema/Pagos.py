from abc import ABC, abstractmethod

# métodos de pago (OCP)
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

    @abstractmethod
    def generar_recibo(self, monto):
        pass
print("Tabla de Metods de pagos\n")
# Método de pago: Tarjeta de Crédito
class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con Tarjeta de Crédito: ""\n")

    def generar_recibo(self, monto):
        return f"Recibo por ${monto} (Tarjeta de Crédito)""\n"

# Método de pago: PayPal
class PayPal(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con PayPal")

    def generar_recibo(self, monto):
        return f"Recibo por ${monto} (PayPal)""\n"

# Método de pago: Nequi
class Nequi(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con Nequi")

    def generar_recibo(self, monto):
        return f"Recibo por ${monto} (Nequi)""\n"

# Clase que procesa pagos (SRP)
class ProcesadorPagos:
    def __init__(self, metodo_pago: MetodoPago):
        self.metodo_pago = metodo_pago

    def realizar_pago(self, monto):
        self.metodo_pago.procesar_pago(monto)
        return self.metodo_pago.generar_recibo(monto)