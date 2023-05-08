# Crear una tupla de numeros
numeros = 1, 2, 3, 4, 5
print (numeros)

elementos = 3, 'a', 8, 7.2, 'hola'
print (elementos)

tup = 1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola'
print (tup)

# Tuple unpacking
bebidas = 'agua', 'café', 'batido'
a, b, c = bebidas
print (a)
print (b)
print (c)

# for tuple Python – Recorrer una tupla
colores = 'azul', 'blanco', 'negro'
for color in colores:
    print(color)

# Modificar una tupla en Python
tupla = (1, ['a', 'b'], 'hola', 8.2)
tupla[1].append('c')  # tupla[1] hace referencia a la lista
print (tupla)

# Longitud (len) de una tupla en Python
vocales = ('a', 'e', 'i', 'o', 'u')
len(vocales)
print (len(vocales))

# Cómo saber si un elemento está en una tupla en Python
colores = 'azul', 'blanco', 'negro'
if 'azul' in colores:
   print('Sí')

if 'verde' not in colores:
   print('No')