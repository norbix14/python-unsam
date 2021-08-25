#!/usr/bin/env python3
# solucion_de_errores.py

import csv
from pprint import pprint

######################################################################
"""
@author: Norberto Fabrizio
"""

# 3

#%% Ejercicio 3.1. Función tiene_a()

# El error era logico, ya que recorre toda la cadena y devuelve la
# ultima comprobacion. No importa si hay al menos una letra `a`, al
# seguir iterando toma el ultimo valor.

# ¿Anda bien en todos los casos de prueba?
"""
def tiene_a(expresion):
  n = len(expresion)
  i = 0
  while i < n:
    if expresion[i] == 'a':
      return True
    else:
      return False
    i += 1
"""

# Corregido
# Lo corregí agregando una variable que guarda si hay alguna letra
# `a` presente y luego salgo del bucle inmediatamente ya que 
# comprobe que existe al menos una letra `a`.
# A continuación va el código corregido:
"""
def tiene_a(expresion):
  n = len(expresion)
  i = 0
  tiene_letra_a = False
  while i < n:
    if expresion[i] == 'a':
      tiene_letra_a = True
      break
    i += 1
  return tiene_letra_a
"""

#%% Ejercicio 3.2. Función tiene_a(), nuevamente

# Tiene errores de sintaxis. Le faltan los dos puntos seguido a la
# definicion de la funcion, los dos puntos despues del bucle `while`,
# usa el operador de asignacion en vez del de comparacion, le faltan
# los dos puntos despues del `if` y al final cuando sale del bucle,
# retorna `Falso` y no `False`.

# ¿Anda bien en todos los casos de prueba?
"""
def tiene_a(expresion)
  n = len(expresion)
  i = 0
  while i < n
    if expresion[i] = 'a'
      return True
    i += 1
  return Falso
"""

# Corregido
def tiene_a(expresion):
  n = len(expresion)
  i = 0
  while i < n:
    if expresion[i] == 'a':
      return True
    i += 1
  return False

#%% Ejercicio 3.3. Función tiene_uno()

# Tiene error al calcular la longitud de `expresion`, ya que no lo 
# puede hacer con un entero.

# ¿Anda bien en todos los casos de prueba?
"""
def tiene_uno(expresion):
  n = len(expresion)
  i = 0
  tiene = False
  while (i<n) and not tiene:
    if expresion[i] == '1':
      tiene = True
    i += 1
  return tiene
"""

# Corregido
# Lo corregi convirtiendo lo que sea que se le pase como parametro,
# a una cadena.
def tiene_uno(expresion):
  expresion = str(expresion)
  n = len(expresion)
  i = 0
  tiene = False
  while (i < n) and not tiene:
    if expresion[i] == '1':
      tiene = True
    i += 1
  return tiene

#%% Ejercicio 3.4. Funcion suma(a, b)

# El error es que la funcion no devuelve ningun valor. Hace el
# calculo pero no lo retorna.

# La siguiente suma no da lo que debería:
"""
def suma(a, b):
  c = a + b
"""

# Corregido
# Simplemente retorno el resultado de la operacion.
def suma(a, b):
  return a + b

#%% Ejercicio 3.5. Funcion leer_camion(nombre_archivo)

# El siguiente ejemplo usa el dataset de la clase anterior,
# pero no lo imprime como corresponde, ¿podés determinar por qué
# y explicarlo brevemente en la versión corregida?
"""
def leer_camion(nombre_archivo):
  camion=[]
  registro={}
  with open(nombre_archivo,"rt") as f:
    filas = csv.reader(f)
    encabezado = next(filas)
    for fila in filas:
      registro[encabezado[0]] = fila[0]
      registro[encabezado[1]] = int(fila[1])
      registro[encabezado[2]] = float(fila[2])
      camion.append(registro)
  return camion
"""

# Corregido
# El error es que, si bien recorre cada fila, solamente se asigna el
# ultimo valor antes de salir del bucle.
# Movi la declaracion de `registro` hacia dentro del bucle `for`,
# de esta manera, por cada iteracion, el registro inicia vacio y
# en cada fila se va llenando con los datos correctos.
def leer_camion(nombre_archivo):
  camion = []
  with open(nombre_archivo, 'rt') as f:
    filas = csv.reader(f)
    encabezado = next(filas)
    for fila in filas:
      registro = {}
      registro[encabezado[0]] = fila[0]
      registro[encabezado[1]] = int(fila[1])
      registro[encabezado[2]] = float(fila[2])
      camion.append(registro)
  return camion

#%% 
if __name__ == '__main__':
  #%% 3.2 - testear tiene_a()
  print('Tiene letra a:', tiene_a('UNSAM 2020'))
  print('Tiene letra a:', tiene_a('abracadabra'))
  print('Tiene letra a:', tiene_a('La novela 1984 de George Orwell'))

  #%% 3.3 - testear tiene_uno()
  print('Tiene a 1:', tiene_uno('UNSAM 2020'))
  print('Tiene a 1:', tiene_uno('La novela 1984 de George Orwell'))
  print('Tiene a 1:', tiene_uno(1984))

  #%% 3.4 - testear suma()
  a, b = 2, 3
  c = suma(a, b)
  print(f'Suma de {a} + {b} = {c}')

  #%% 3.5 - testear leer_camion()
  camion = leer_camion('../Data/camion.csv')
  pprint(camion)
