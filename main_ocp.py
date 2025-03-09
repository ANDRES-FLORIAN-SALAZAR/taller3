from ocp.Calculadora import CalculadoraDescuentos
from ocp.Descuento import DescuentoRegular, DescuentoVIP, BlackFridayDescuento

precio = 100
print("¡Bienvenido a la tabla de descuentos!\n")
# Calcular precio con descuento regular
calculadora_regular = CalculadoraDescuentos(DescuentoRegular())
print(f"Precio con descuento regular: {calculadora_regular.calcular_precio_final(precio)}\n")

# Calcular precio con descuento VIP
calculadora_vip = CalculadoraDescuentos(DescuentoVIP())
print(f"Precio con descuento VIP: {calculadora_vip.calcular_precio_final(precio)}\n")

# Calcular precio con descuento Black Friday
calculadora_black_friday = CalculadoraDescuentos(BlackFridayDescuento())
print(f"Precio con descuento Black Friday: {calculadora_black_friday.calcular_precio_final(precio)}")