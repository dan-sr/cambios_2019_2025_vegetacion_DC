def saludo(nombre):
    return f"Hola, {nombre}! Bienvenido a la práctica de git."


def contar_palabras(texto):
    return len(texto.split())


if __name__ == "__main__":
    mensaje = saludo("estudiante")
    print(mensaje)
    print(f"El saludo tiene {contar_palabras(mensaje)} palabras.")
