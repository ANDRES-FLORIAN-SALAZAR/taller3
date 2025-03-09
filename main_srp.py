from srp.Usuario import Usuario, Autenticador, Notificador

# Crear un usuario
usuario = Usuario(": Juan", ": juan@example.com ")

# Autenticar al usuario
autenticador = Autenticador()
autenticador.autenticar(usuario, "password123")

# Enviar un mensaje al usuario
notificador = Notificador()
notificador.enviar_mensaje(usuario, "\n¡Bienvenido al sistema!")