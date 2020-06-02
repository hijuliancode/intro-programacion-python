# Revisar si una condición es mayor a
balance = 0
if balance > 0:
  print('Puedes pagar')
else:
  print('No tienes saldo')

# IF con texto
lenguaje = 'Python'
if lenguaje == 'Python':
  print('Excelente decisión')

## !== en Python es = a : not
if not lenguaje == 'Java':
  print('Excelente decisión')

# Evaluar Boolean
usuario_autenticado = True

if usuario_autenticado:
  print('El usuario esta autenticado')
else:
  print('El usuario no esta autenticado')

#Evaluar elementos de una lista
lenguajes = ['Python', 'JavaScript', 'Dart', 'C++', 'Ruby']
if not 'PHP' in lenguajes:
  print('No se encuentra en la lista')
else:
  print('Si se encuentra en la lista')

# If anidados
usuario_autenticado = True
usuario_admin = False

if usuario_autenticado:
  if usuario_admin:
    print('Acceso Total!')
  else:
    print('El usuario esta autenticado')
else:
  print('El usuario no esta autenticado')

# elif
ocupacion = 'Estudiante'

if ocupacion == 'Estudiante':
  print('Tiene un descuento del 50%')
elif ocupacion == 'Jubilado':
  print('Tiene un descuento del 75%')
elif ocupacion == 'Desempleado':
  print('Tiene un descuento del 15%')
else:
  print('Debe pagar el 100%')
