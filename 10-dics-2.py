jugador = {}
print(jugador)

# Se une un jugador
jugador['nombre'] = 'Julian'
jugador['puntaje'] = 0
print(jugador)

# Incrementando Puntaje
jugador['puntaje'] = 100
print(jugador)
# Incrementando Puntaje
jugador['puntaje'] = 200
print(jugador)


# Acceder a un valor que no existe
print(jugador.get('consola'))
print(jugador.get('consola', 'No existe ese valor'))

# Iterar en el diccionario
for llave, valor in jugador.items():
    print(f'llave: {llave}')
    print(f'valor: {valor}')

# Eliminar jugador y puntaje
del jugador['nombre']
del jugador['puntaje']

print(jugador)
