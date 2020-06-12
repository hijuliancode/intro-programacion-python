### Imprimir Nombre
# nombre = input('¿Cuál es tu nombre?: \r\n')
# print(f'Hola {nombre}!')


### Leer datos que serán números
# edad = input('¿Cuál es tu edad?: \r\n')
#   # Convertir edad (string) a número entero (int)
#   edad = int(edad)

# if edad >= 18:
#   print('Ya puedes votar')
# else:
#   print('Aún no puedes votar')

### Mezclando con operadores
# numero = input('Agrega un número y te diré si es par o impar: \r\n')
# numero = int(numero)
# if numero % 2 == 0:
#   print(f'El numero {numero} es par')
# else:
#   print(f'El número {numero} es impar')

### RETO
# Realiza un examen con 3 preguntas que tu desees,
# el usuario deberá responder "SI" o "NO" y al final otorgarle una calificación
# (La calificación se logra con una variable que inicia en 0
# y por cada respuesta correcta incrementa en 1)
nota = 0
pregunta1 = input('¿El vidrio es transparente?: \r\n')
pregunta2 = input('¿JavaScript es lo mismo que Java?: \r\n')
pregunta3 = input('¿Las variables y las funciones se procesan antes de ejecutar cualquier trozo de código?: \r\n')

if pregunta1 == 'SI':
  nota += 1
if pregunta2 == 'NO':
  nota += 1
if pregunta3 == 'SI':
  nota += 1

print(f'Nota final: {nota}')
