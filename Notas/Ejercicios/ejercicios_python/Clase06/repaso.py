#!/usr/bin/env python3
# repaso.py

######################################################################

# 6.1 - Repaso de temas pasados

#%% 6.1 - propagar por vecinos
#
def propagar_al_vecino(lista):
  modificado = False
  n = len(lista)
  for i, e in enumerate(lista):
    if (e == 1) and (i < n - 1) and (lista[i + 1] == 0):
      lista[i + 1] = 1
      modificado = True
    if (e == 1) and (i > 0) and (lista[i - 1] == 0):
      lista[i - 1] = 1
      modificado = True
  return modificado
#
def propagar_61(lista):
  m = lista.copy()
  veces = 0
  while propagar_al_vecino(lista):
    veces += 1
  print(f'Repetí {veces} veces la función propagar_al_vecino')
  print(f'Con input {m}')
  print(f'Y obtuve {lista}')
  return m

#%% 6.2 - propagar como el auto fantastico
#
def propagar_a_derecha(l):
  lista = l.copy()
  n = len(lista)
  for i, e in enumerate(lista):
    if (e == 1) and (i < n - 1):
      if (lista[i + 1] == 0):
        lista[i + 1] = 1
  return lista
#
def propagar_a_izquierda(lista):
  l = lista[::-1]
  lpd = propagar_a_derecha(l)
  return lpd[::-1]
#
def propagar_62(lista):
  ld = propagar_a_derecha(lista)
  lp = propagar_a_izquierda(ld)
  return lp

#%% 6.3 - propagar con cadenas
#
def traducir_lista_a_cadena(lista):
  """traduce una lista con 1, 0 y -1 a una cadena con 'f', 'o', 'x'."""
  diccionario = {
    1: 'f',
    0: 'o',
    -1: 'x'
  }
  cadena = ''.join(
    [
      diccionario[el]
      for el in lista
    ]
  )
  return cadena
#
def traducir_cadena_a_lista(cadena):
  """traduce cadena con 'f', 'o' y 'x' a una lista con 1, 0 y -1."""
  diccionario = {
    'f': 1,
    'o': 0,
    'x': -1
  }
  lista = [
    diccionario[char]
    for char in cadena
  ]
  return lista
#
def propagar_63(lista, debug = True):
  cadena = traducir_lista_a_cadena(lista)
  if debug:
    print(cadena)#, end = ' -> ')
  fosforos_utiles = cadena.split('x')
  lista_propagada = [
    fosforo
    if ('f' not in fosforo) else 'f'*len(fosforo)
    for fosforo in fosforos_utiles
  ]
  cadena_propagada = 'x'.join(lista_propagada)
  if debug:
    print(cadena_propagada)
  return traducir_cadena_a_lista(cadena_propagada)
