## Funciones: funcion()
## Metodos: Funciones dentro de un objeto objeto.metodo()

nombre = 'julian'

def mostrar_nombre(nombre):
    print(f'Hola {nombre}')

# mostrar_nombre(nombre)
# mostrar_nombre(nombre.upper())
# mostrar_nombre(nombre.title())

# Retos
## 00 Crea una función que imprima un mensaje de bienvenida
## 01 Crea una función que tome un nombre de usuario y lo muestre como mensaje de bienvenida
## 00 Crea una función que tome la ultima actividad que hiciste

#01
def mensaje_bienvenida():
    print('Hola, Bienvenid@')

mensaje_bienvenida()

#02
usuario = 'Meraki'

def mensaje_usuario(usuario = 'desconocido'):
    print(f'Hola {usuario}, bienvenido/a')

mensaje_usuario()
mensaje_usuario('Julian')

#03
def mostrar_ultima_actividad(actividad = 'descansar'):
    print(f'Mi ultima actividad fue {actividad}')

mostrar_ultima_actividad()
mostrar_ultima_actividad('cocinar')
mostrar_ultima_actividad('aprender')
