#!/usr/bin/env python3
# plot_bbin_vs_bsec.py

import random
import matplotlib.pyplot as plt
import numpy as np

######################################################################
"""
@author: Norberto Fabrizio
"""

# 6.7 - Graficos de complejidad

#%% contar cantidad de operaciones de un algoritmo
def busqueda_secuencial_(lista, x):
  """Si `x` está en la `lista` devuelve el índice de su primera aparición,
  de lo contrario devuelve `-1`. Además devuelve la cantidad de
  comparaciones que hace la función.

  Parametros:
    `lista` (list): listado de elementos.
    `x` (int): elemento a buscar en el listado.

  Ejemplo:
    >>> lista = [1,3,5,7,2,8,9,6]
    >>> busqueda_secuencial_(lista, 9)
    # devuelve una tupla como (posicion, comparaciones)
    (6, 7)
  """
  comps = 0
  pos = -1
  for i, z in enumerate(lista):
    comps += 1
    if (z == x):
      pos = i
      break
  return pos, comps

#%% 6.19
#
def busqueda_binaria(lista, x, verbose = False):
  """Búsqueda binaria.

  Precondición: la `lista` está ordenada.
  Devuelve -1 si `x` no está en la `lista`.
  Devuelve `p` tal que `lista[p] == x`, si `x` está en la `lista`.

  Parametros:
    `lista` (list): listado ordenado de elementos.
    `x` (int): elemento a buscar dentro de la lista.
    `verbose` (bool): ver operaciones realizadas si es True.

  Ejemplo:
    >>> lista = [1, 3, 5]
    >>> busqueda_binaria(lista, 0)
    (-1, 2)
    >>> busqueda_binaria(lista, 6)
    (-1, 2)
    >>> busqueda_binaria(lista, 3)
    (1, 2)
  """
  if verbose:
    print(f'[DEBUG] izq |der |medio')
  pos = -1
  izq = 0
  der = len(lista) - 1
  comps = 0
  while (izq <= der):
    comps += 1
    medio = (izq + der) // 2
    if verbose:
      print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
    if (lista[medio] == x):
      pos = medio
    if (lista[medio] > x):
      der = medio - 1
    else:
      izq = medio + 1
  return pos, comps
#
def generar_lista(n, m):
  """Generar una lista ordenada de elementos diferentes entre 
  `0` y `m - 1`.

  Parametros:
    `n` (int): cantidad de elementos a generar.
    `m` (int): rango en el que deben estar los elementos.

  Ejemplo:
    >>> generar_lista(10, 100)
    [5, 9, 14, 38, 46, 58, 68, 78, 86, 95]
  """
  l = random.sample(range(m), k = n)
  l.sort()
  return l
#
def generar_elemento(m):
  """Devolver un elemento aleatorio en el rango de `m - 1`.

  Parametros:
    `m` (int): rango en el que debe estar el elemento.

  Ejemplo:
    >>> generar_elemento(100)
    88
  """
  return random.randint(0, m - 1)
#
def experimento_elemental():
  """Experimento elemental.

  Dada una lista ya generada, digamos que un `experimento elemental`
  es generar un elemento, buscarlo en la lista y contar la cantidad
  de comparaciones realizadas. Esta cantidad de operaciones es el
  `resultado` del experimento elemental.
  """
  m = 10000
  n = 100
  lista = generar_lista(n, m)
  # aca comienza el experimento
  x = generar_elemento(m)
  comps = busqueda_secuencial_(lista, x)[1]
  return comps
#
def experimento_secuencial_promedio(lista, m, k):
  """Mostrar las comparaciones promedio.

  Parametros:
    `lista` (list): listado ordenado de elementos.
    `m` (int): rango en el que debe estar el elemento.
    `k` (int): cantidad de comparaciones.

  Ejemplo:
    >>> m = 10000
    >>> n = 100
    >>> k = 1000
    >>> lista = generar_lista(n, m)
    >>> experimento_secuencial_promedio(lista, m, k)
    99.625
  """
  comps_tot = 0
  for i in range(k):
    x = generar_elemento(m)
    comps_tot += busqueda_secuencial_(lista, x)[1]
  comps_prom = comps_tot / k
  return comps_prom
#
def graficar_experimentos_promedios():
  """Graficar los experimentos.

  Si decíamos que buscar un elemento era un `experimento elemental`
  digamos que repetir `k` experimentos elementales y calcular el
  promedio de comparaciones es un `experimento de promedios`.
  """
  m = 10000
  k = 1000
  largos = np.arange(256) + 1
  comps_promedio = np.zeros(256)
  for i, n in enumerate(largos):
    lista = generar_lista(n, m)
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)
  plt.plot(largos, comps_promedio, label='Busqueda Secuencial')
  plt.xlabel('Largo de la lista')
  plt.ylabel('Cantidad de comparaciones')
  plt.title('Complejidad de la busqueda')
  plt.legend()
  plt.show()
  return None

#%% 6.20 - busqueda binaria vs busqueda secuencial
#
def experimento_binario_promedio(lista, m, k):
  """Mostrar las comparaciones promedio.

  Parametros:
    `lista` (list): listado ordenado de elementos.
    `m` (int): rango en el que debe estar el elemento.
    `k` (int): cantidad de comparaciones.

  Ejemplo:
    >>> m = 10000
    >>> n = 100
    >>> k = 1000
    >>> lista = generar_lista(n, m)
    >>> experimento_binario_promedio(lista, m, k)
    6.677
  """
  comps_tot = 0
  for i in range(k):
    x = generar_elemento(m)
    comps_tot += busqueda_binaria(lista, x)[1]
  comps_prom = comps_tot / k
  return comps_prom
#
def graficar_bbin_vs_bseq(m = 10000, k = 1000):
  """Generar y graficar un experimento.

  Parametros:
    `m` (int): rango en el que deben estar los elementos.
    `k` (int): cantidad de comparaciones.

  Ejemplo:
    >>> graficar_bbin_vs_bseq()
    # muestra plot con parametros por defecto
  """
  largos = np.arange(256) + 1
  comps_sec_prom = np.zeros(256)
  comps_bin_prom = np.zeros(256)
  xlim = ylim = len(largos) + 10
  for i, n in enumerate(largos):
    lista = generar_lista(n, m)
    comps_sec_prom[i] = experimento_secuencial_promedio(lista, m, k)
    comps_bin_prom[i] = experimento_binario_promedio(lista, m, k)
  plt.plot(largos, comps_sec_prom, label='Busqueda Secuencial')
  plt.plot(largos, comps_bin_prom, label='Busqueda Binaria')
  plt.xlabel('Largo de la lista')
  plt.xlim(0, xlim)
  plt.ylabel('Cantidad de comparaciones')
  plt.ylim(0, ylim)
  plt.title('Complejidad de la busqueda')
  plt.legend()
  plt.show()
  return None
