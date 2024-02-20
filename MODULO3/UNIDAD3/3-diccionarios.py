notas = {"Camila": 7, "Antonio": 5, "Felipe": 6, "Antonia": 7}

# Imprimir diccionarios
print(notas)

# Buscar el valor por medio de la llave
print(notas["Felipe"])  # 6

# Llave erronea debe ser exactamente igual
print(notas["felipe"])  # KeyError: 'felipe'

# Llaves duplicadas, regresan el ultimo valor
duplicados = {"clave": 1, "clave": 2}
print(duplicados)  # {"clave": 2}

# Agregar una llave
diccionario = {"llave 1": 5}
diccionario["llave 2"] = 9
print(diccionario)  # {"llave 1": 5, "llave 2": 9}

# Cambiar un elemento del diccionario
diccionario = {"llave 1": 5, "llave 2": 7}
diccionario["llave 2"] = 9
print(diccionario)  # {"llave 1": 5, "llave 2": 9}

# Eliminar un elemento del diccionario
diccionario = {"celular": 140000, "notebook": 489990, "tablet": 120000, "cargador": 12400}
del diccionario["celular"]
print(diccionario)

