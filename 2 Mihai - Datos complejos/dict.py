# Cómo crear un diccionario
d = {1: 'hola', 89: 'Pythonista', 'a': 'b', 'c': 27}
print (d)

# Cómo acceder a los elementos de un diccionario en Python
d = {'uno': 1, 'dos': 2, 'tres': 3}
print (d['dos'])

# Añadir elementos a un diccionario en Python
d = {'uno': 1, 'dos': 2}
d['tres'] = 3
print (d)
# También existe el método setdefault(clave[, valor]).
d.setdefault('tres', 3)
print (d)
d.setdefault('cuatro')
print (d)

# Modificar elementos de un diccionario
d = {'uno': 1, 'dos': 2}
d['uno'] = 1.0
print (d)

# Eliminar un elemento de un diccionario en Python
d = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}
del d['tres']
print (d)

# Comprobar si un elemento está en un diccionario en Python
print('uno' in d)
print(1 in d)
print(1 not in d)
# Intenta eliminar la clave 1 si existe
if 1 in d:
    del d[1]
print (d)

# Comparar si dos diccionarios son iguales
d1 = {'uno': 1, 'dos': 2}
d2 = {'dos': 2, 'uno': 1}
d3 = {'uno': 1}
print(d1 == d2)
print(d1 == d3)