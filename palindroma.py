# Rafael Miranda Jimenez
# Ejercicio para saber si una palabra es palindroma o no
def es_palindroma(palabra):
    # Convertir la palabra a minúsculas y eliminar espacios
    palabra = palabra.lower().replace(" ", "")
    # Comprobar si la palabra es igual a su versión invertida
    return palabra == palabra[::-1]

# Solicitar al usuario que ingrese una palabra
palabra_usuario = input("Ingresa una palabra: ")

# Verificar si es palíndroma y mostrar el resultado
if es_palindroma(palabra_usuario):
    print(f"La palabra '{palabra_usuario}' es palíndroma.")
else:
    print(f"La palabra '{palabra_usuario}' no es palíndroma.")
