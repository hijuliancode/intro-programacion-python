continuar = True
pregunta = 'Escribe un número y te diré si es par o impar '
pregunta += '(cerrar para salir de la aplicación) \r\n'

while continuar:
  entrada = input(pregunta)
  if entrada == 'cerrar' or entrada == 'salir':
    continuar = False
    print('¡Buen juego, adios!')
  else:
    entrada = int(entrada)
    if entrada % 2 == 0:
      print('Número Par')
    else:
      print('Número Impar')
