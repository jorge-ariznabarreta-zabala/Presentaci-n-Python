# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan
c = {1, 3, 2, 9, 3, 1}
print (c)

# Crea un conjunto a partir de un string
# Los caracteres repetidos se eliminan
a = set('Hola Pythonista')
print (a)

# Para crear un conjunto de tipo frozenset, se usa el constructor de la clase frozenset():
f = frozenset([3, 5, 6, 1, 5])
print (f)

# Añadir elementos a un conjunto (set) en Python
# Añade el elemento 7 al conjunto
mi_conjunto = {1, 3, 2, 9, 3, 1}
mi_conjunto.add(7)
print (mi_conjunto)

# Añade los elementos 5, 3, 4 y 6 al conjunto
# Los elementos repetidos no se añaden al conjunto
mi_conjunto.update([5, 3, 4, 6])
print (mi_conjunto)

# Eliminar un elemento de un conjunto en Python
mi_conjunto1 = {1, 3, 2, 9, 3, 1, 6, 4, 5}
print (mi_conjunto1)

# Elimina el elemento 1 con remove()
mi_conjunto1.remove(1)
print (mi_conjunto1)

# Elimina el elemento 4 con discard()
mi_conjunto1.discard(4)
print (mi_conjunto1)

# Obtiene y elimina un elemento aleatorio con pop()
mi_conjunto1.pop()
print (mi_conjunto1)
# Elimina todos los elementos del conjunto
mi_conjunto1.clear()
print (mi_conjunto1)

# Unión de conjuntos en Python
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print (a | b)

# Intersección de conjuntos en Python
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print (a & b)

# Diferencia de conjuntos en Python (todos los elementos que contiene a y no tiene b)
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print (a - b)

# Diferencia simétrica de conjuntos en Python ( contiene los elementos de A y B que no son comunes)
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print (a ^ b)



