## En Python no existen arrays, existen list
lenguajes = ['Python', 'JavaScript', 'Dart', 'C++']

print(lenguajes)
print(lenguajes[0]) # Los List inician en la posición 0
print(lenguajes[1])
print(lenguajes[2])
print(lenguajes[3])
# print(lenguajes[4]) # ERROR: Index fuera del rango de la lista

# Algunos metodos de lists
lenguajes.sort() # Ordena los elementos de la lista alfabeticamente
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendio = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendio)

# Modificando valores de un arreglo (acceder a la posición y reemplazar)
lenguajes[0] = 'Typescript'
print(lenguajes)

# Agregar elementos a un list
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar de un list
del lenguajes[0]
print(lenguajes)

# Eliminar de un list con .pop (elimina la última posición de la lista)
lenguajes.pop()
print(lenguajes)

# Eliminar de un list con .pop(argumento)
lenguajes.pop(1)
print(lenguajes)

# Eliminar de un list por nombre
lenguajes.remove('Python')
print(lenguajes)
