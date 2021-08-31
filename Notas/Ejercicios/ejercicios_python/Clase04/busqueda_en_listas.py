#!/usr/bin/env python3
# busqueda_en_listas.py

######################################################################
"""
@author: Norberto Fabrizio
"""

# 4.2

#%% 4.3 - busquedas de un elemento
def buscar_u_elemento(lista = [], elemento = 0):
  """Buscar un elemento en la lista.

  Debe devolver el indice en donde se encuentra el elemento o -1
  si no lo encuentra.

  Parametros:
    `lista` (list): lista de elementos.
    `elemento` (any): elemento a buscar.

  Ejemplo:
    >>> lista = [1,2,3,2,3,4]
    >>> print(buscar_u_elemento(lista, 1))
    0
    >>> print(buscar_u_elemento(lista, 5))
    -1
  """
  pos = -1
  if(type(lista) is list):
    if len(lista) <= 0:
      return pos
    for i, item in enumerate(lista):
      if (item == elemento):
        pos = i
        break
  return pos

def buscar_n_elemento(lista = [], elemento = 0):
  """Buscar un elemento en la lista.

  Debe devolver cuantas veces se encontro el elemento en la lista.

  Parametros:
    `lista` (lista): lista de elementos.
    `elemento` (any): elemento a buscar.

  Ejemplo:
    >>> lista = [1,2,3,2,3,4]
    >>> print(buscar_n_elemento(lista, 2))
    2
    >>> print(buscar_n_elemento(lista, 5))
    0
  """
  veces = 0
  if(type(lista) is list):
    if len(lista) <= 0:
      return veces
    for i, item in enumerate(lista):
      if (item == elemento):
        veces += 1
  return veces

#%% 4.4 - busqueda de maximo y minimo
def maximo(lista = []):
  """Devuelve el maximo de la lista.

  La lista no debe estar vacia y deben ser numeros positivos.

  Parametros:
    `lista` (list): lista de elementos.

  Ejemplo:
    >>> lista = [10,2,70,5,10,84,20,30,33,50]
    >>> print(maximo(lista))
    84
  """
  if (type(lista) is list):
    if (len(lista) <= 0):
      return lista
    m = lista[0]
    for i in lista:
      if (i >= m):
        m = i
    return m
  return lista

def minimo(lista = []):
  """Devuelve el minimo de la lista.

  La lista no debe estar vacia y deben ser numeros positivos.

  Parametros:
    `lista` (list): lista de elementos.

  Ejemplo:
    >>> lista = [10,2,70,5,10,84,20,30,33,50]
    >>> print(minimo(lista))
    2
  """
  if (type(lista) is list):
    if (len(lista) <= 0):
      return lista
    m = lista[0]
    for i in lista:
      if (i <= m):
        m = i
    return m
  return lista
