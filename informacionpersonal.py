# Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
print("Ciudad original:", informacion_personal["ciudad"])  # Imprimir ciudad original
informacion_personal["ciudad"] = "Guayaquil"  # Modificar la ciudad
print("Ciudad modificada:", informacion_personal["ciudad"])  # Imprimir ciudad modificada

# Agregar una nueva clave-valor al diccionario
informacion_personal["telefono"] = "0987654321"  # Agregar número de teléfono
print("Número de teléfono agregado:", informacion_personal["telefono"])  # Imprimir teléfono

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Agregar si no existe
else:
    print("La clave 'telefono' ya existe en el diccionario.")

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar la edad
    print("La clave 'edad' ha sido eliminada.")
else:
    print("La clave 'edad' no existe en el diccionario.")

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
