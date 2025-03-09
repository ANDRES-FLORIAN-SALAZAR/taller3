from sistema.Pagos import ProcesadorPagos, TarjetaCredito, PayPal, Nequi

monto = 100

# Procesar pago con Tarjeta de Crédito
procesador_tarjeta = ProcesadorPagos(TarjetaCredito())
print(procesador_tarjeta.realizar_pago(monto))

# Procesar pago con PayPal
procesador_paypal = ProcesadorPagos(PayPal())
print(procesador_paypal.realizar_pago(monto))

# Procesar pago con Nequi
procesador_nequi = ProcesadorPagos(Nequi())
print(procesador_nequi.realizar_pago(monto))