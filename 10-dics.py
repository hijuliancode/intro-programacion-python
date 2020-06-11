# Creando un diccionario simple
cancion = {
  'artista': 'Metallica',
  'cancion': 'Enter Sadman',
  'lanzamiento': 1992,
  'likes': 3000
}

print(cancion)

# Acceder a los elementos del diccionario
print(cancion['cancion'])
print(cancion['lanzamiento'])

# Mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando {artista}')

# Agregar nuevos valores
print(cancion)
cancion['playlist'] = 'Heavy Metal'
print(cancion)

# Reemplazar valor
cancion['cancion'] = 'Seek and Destroy'
print(cancion)

# Eliminar un valor
del cancion['lanzamiento']
print(cancion)
