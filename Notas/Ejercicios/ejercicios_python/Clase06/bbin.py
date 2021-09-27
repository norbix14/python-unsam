#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bbin.py
"""
@author: Norberto Fabrizio
"""

# 6.5 - Busqueda binaria

#%% 
def algoritmo_cuadratico(lista, m):
  """Este algoritmo realiza una comparación `m == p*q` para cada
  elemento `p` y cada elemento `q` de la lista. Es decir, realiza
  `n*n = n^2` comparaciones. Es un algoritmo cuadrático.
  Su complejidad es `O(n^2)`.

  Parametros:
    `lista` (list): listado de elementos.
    `m` (int): valor que queremos comparar.
  """
  comps = 0
  n = len(lista)
  for p in lista:
    for q in lista:
      comps += 1
      if (m == (p * q)):
        print("%d = %d * %d" % (m, p, q))
  print(f'Longitud de la lista: {n}')
  print(f'Cantidad de comparaciones: {comps}')
  print(f'Complejidad O({n}^2) = {n**2}')

#%% 6.13 
def busqueda_binaria(lista, x, verbose = False):
  """Búsqueda binaria.

  Precondición: la lista está ordenada.
  Devuelve -1 si x no está en lista.
  Devuelve p tal que lista[p] == x, si x está en lista.

  Parametros:
    `lista` (list): listado ordenado de elementos.
    `x` (int): elemento a buscar dentro de la lista.
    `verbose` (bool): ver operaciones realizadas si es True.

  Ejemplo:
    >>> lista = [1, 3, 5]
    >>> busqueda_binaria(lista, 0)
    -1
    >>> busqueda_binaria(lista, 6)
    -1
    >>> busqueda_binaria(lista, 3)
    1
  """
  if verbose:
    print(f'[DEBUG] izq |der |medio')
  pos = -1
  izq = 0
  der = len(lista) - 1
  while (izq <= der):
    medio = (izq + der) // 2
    if verbose:
      print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
    if (lista[medio] == x):
      pos = medio
    if (lista[medio] > x):
      der = medio - 1
    else:
      izq = medio + 1
  return pos

#%% 6.14 
def donde_insertar(lista, x, verbose = False):
  """Buscar donde insertar `x` en `lista` y mantenerla ordenada.

  Parametros:
    `lista` (list): listado ordenado de elementos.
    `x` (int): elemento a insertar dentro de la lista.
    `verbose` (bool): ver operaciones realizadas si es True.

  Ejemplo:
    >>> lista = [0, 2, 4, 6]
    >>> donde_insertar(lista, 3)
    2
    >>> donde_insertar(lista, 4)
    2
    >>> donde_insertar(lista, 7)
    4
    >>> donde_insertar(lista, 10)
    4
    >>> donde_insertar(lista, 100)
    4
  """
  pos = -1
  izq = 0
  der = len(lista) - 1
  if verbose:
    print(f'[DEBUG] izq |der |medio')
  while (izq <= der):
    medio = (izq + der) // 2
    if verbose:
      print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
    if (lista[medio] >= x):
      der = medio - 1
      pos = medio
    else:
      izq = pos = medio + 1
  return pos

#%% 6.15 
def insertar(lista, x):
  """Insertar `x` en `lista` y mantenerla ordenada.

  Parametros:
    `lista` (list): listado ordenado de elementos.
    `x` (int): elemento a insertar dentro de la lista.

  Ejemplo:
    >>> lista = [0, 2, 4, 6]
    >>> insertar(lista, 3)
    2
    >>> lista
    [0, 2, 3, 4, 6]
    >>> insertar(lista, 4)
    3
    >>> lista
    [0, 2, 3, 4, 6]
    >>> insertar(lista, 5)
    4
    >>> lista
    [0, 2, 3, 4, 5, 6]
    >>> insertar(lista, 10)
    6
    >>> lista
    [0, 2, 3, 4, 5, 6, 10]
  """
  izq = 0
  der = len(lista) - 1
  existe = False
  while (izq <= der):
    medio = (izq + der) // 2
    if (lista[medio] >= x):
      der = medio - 1
      pos = medio
      existe = True if (lista[medio] == x) else False
    else:
      izq = pos = medio + 1
  if not existe:
    lista.insert(pos, x)
  return pos

#%% 6.16 - calcular complejidad de propagar

#%% 6.17 
def incrementar(secuence, verbose = False):
  """Calcular la secuencia siguiente de una secuencia dada.

  Parametros:
    `secuence` (list): secuencia.
    `verbose` (bool): si es True, muestra las comparaciones realizadas.

  Ejemplo:
    >>> secuence = [0,0,1,0,0]
    >>> incrementar(secuence)
    [0, 0, 1, 0, 1]
  """
  carry = 1
  leng = len(secuence)
  comps = 0
  for i in range(leng-1,-1,-1):
    comps += 1
    if (secuence[i] == 1) and (carry == 1):
      secuence[i] = 0
      carry = 1
    else:
      secuence[i] = secuence[i] + carry
      carry = 0
  if verbose:
    print(f'Comparaciones: {comps}')
  return secuence

#%% 6.18 
def listar_secuencias(n = 4, verbose = False):
  """Mostrar listado de secuencias binarias.

  Parametros:
    `n` (int): longitud.
    `verbose` (bool): si es True, muestra cuantas comparaciones se realizaron.

  Ejemplo:
    >>> from pprint import pprint
    >>> pprint(listar_secuencias())
    # por defecto, n = 4
    [[0, 0, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 0],
     [0, 0, 1, 1],
     [0, 1, 0, 0],
     [0, 1, 0, 1],
     [0, 1, 1, 0],
     [0, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 0, 0, 1],
     [1, 0, 1, 0],
     [1, 0, 1, 1],
     [1, 1, 0, 0],
     [1, 1, 0, 1],
     [1, 1, 1, 0],
     [1, 1, 1, 1]]
  """
  secuencias = []
  comps = 0
  lista = [0] * n
  while not (lista == [1] * n):
    secuencias.append(lista.copy())
    incrementar(lista)
    if (lista == [1] * n):
      secuencias.append(lista.copy())
    comps += 1
  if verbose:
    print(f'Comparaciones: {comps}')
  return secuencias
