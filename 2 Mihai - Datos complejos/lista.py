# Crear una lista de numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (numeros)

elementos = [3, 'a', 8, 7.2, 'hola']
print (elementos)

# Cómo acceder a los elementos de una lista en Python
lista = ['a', 'b', 'd', 'i', 'j']
print (lista[0])  # Primer elemento de la lista. Índice 0
print (lista[3])  # Cuarto elemento de la lista. Índice 3

# Acceso a los elementos usando un índice negativo
vocales = ['a', 'e', 'i', 'o', 'u']
print (vocales[-1])
#vocales ([-4]) - va a dar error

# Añadir elementos a una lista en Python

vocales = ['a']
vocales.append('e')  # Añade un elemento
print (vocales)

vocales.extend(['i', 'o', 'u'])  # Añade un grupo de elementos
print (vocales)

# Modificar elementos de una lista
 
vocales = ['o', 'o', 'o', 'o', 'u']
# Actualiza el elemento del índice 0
vocales[0] = 'a'
print (vocales)

# Actualiza los elementos entre las posiciones 1 y 2
vocales[1:3] = ['e', 'i']
print (vocales)

# Eliminar un elemento de una lista en Python

# Elimina el elemento del índice 1
vocales = ['a', 'e', 'i', 'o', 'u']
del vocales[1]
print (vocales)

# Elimina los elementos con índices 2 y 3
vocales = ['a', 'e', 'i', 'o', 'u']
del vocales[2:4]
print (vocales)

# Elimina todos los elementos
del vocales[:]
print (vocales)
