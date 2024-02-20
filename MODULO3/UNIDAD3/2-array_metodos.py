# Declaramos la variable
colores = ['verde', 'rojo', 'rosa', 'azul']
numeros = [2, 5, 1, 4, 3]
# Append agrega un elemento a una lista
colores.append("celeste")

# Insert agrega un elemento en una posición específica
colores.insert(2, "amarillo")

# Pop elimina un elemento de una lista
color = colores.pop(3)

# Remove elimina un elemento de una lista
colores.remove("rojo")

# reverse invierte los elementos de una lista
colores.reverse()

# sort ordena los elementos de una lista
numeros_ordenados = sorted(numeros)

# len devuelve la longitud de una lista
longitud = len(colores)

# index devuelve el índice de un elemento en una lista
indice = colores.index("azul")

# Para crear una lista combinada solo debes concatenar las listas
nueva_lista = colores + numeros

# Para repetir una lista solo debes multiplicarla por un número
lista_duplicada = colores * 5

print(colores)
print(color)
print(numeros)
print(numeros_ordenados)
print(longitud)
print(indice)
print(nueva_lista)
print(lista_duplicada)
