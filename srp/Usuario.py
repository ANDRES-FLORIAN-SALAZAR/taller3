# Clase que maneja la información del usuario (SRP)
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

# Clase que maneja la autenticación (SRP)
class Autenticador:
    def autenticar(self, usuario, contraseña):
        
        if contraseña == "password123":
            print(f"Usuario {usuario.nombre} \n¡autenticado correctamente!")
            return True
        else:
            print("Error: Contraseña incorrecta.")
            return False

# Clase que maneja las notificaciones (SRP)
class Notificador:
    def enviar_mensaje(self, usuario, mensaje):
        # Lógica de notificación simulada
        print(f"Enviando correo de autenticación a {usuario.email}: {mensaje}")