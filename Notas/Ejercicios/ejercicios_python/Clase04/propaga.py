#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# propaga.py
"""
@author: Norberto Fabrizio
"""

# 4.6

#%% invertir_lista()
def invertir_lista(lista = []):
  """Mostrar la lista invertida.

  Parametros:
    `lista` (list): lista de elementos.

  Ejemplo:
    >>> invertir_lista([1, 2, 3, 4, 5])
    [5,4,3,2,1]
    >>> invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
    ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
    >>> invertir_lista([])
    []
  """
  if (type(lista) is list):
    if (len(lista) <= 0):
      return []
    invertida = []
    i = len(lista) - 1
    for _ in lista:
      invertida.append(lista[i])
      i -= 1
    return invertida
  return lista

#%% propagar()
def propagar(vector = []):
  """Mostrar un nuevo vector pero propagado.

  Parametros:
    `vector` (list): vector de elementos.

  Ejemplo:
    >>> propagar([0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0])
    [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
    >>> propagar([0, 0, 0, 1, 0, 0])
    [1, 1, 1, 1, 1, 1]
  """
  if (type(vector) is list):
    if (len(vector) <= 0):
      return []
    for r in ['start', 'end']:
      if r == 'start':
        copia = list(vector)
      if r == 'end':
        vector = invertir_lista(copia)
        copia = list(vector)
      prev = vector[0]
      for i, el in enumerate(vector):
        if el == 0:
          if prev == 1:
            copia[i] = 1
            prev = 1
        elif el == 1:
          if prev == 0:
            copia[i] = 1
            prev = 1
          else:
            prev = 1
        else:
          prev = el
    return invertir_lista(copia)
  return vector

#%%
def main():
  """Main. Ejecutar algunas pruebas."""
  # ejemplos clase
  vector1 = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
  vector2 = [0, 0, 0, 1, 0, 0]
  print('ORIGINAL ', vector1)
  print('PROPAGADO', propagar(vector1))
  print()
  print('ORIGINAL ', vector2)
  print('PROPAGADO', propagar(vector2))
  print()
  # ejemplos
  vector3 = [-1, -1, 0, 1, 0, -1]
  vector4 = [-1, 1, 0, -1, 0, -1]
  print('ORIGINAL ', vector3)
  print('PROPAGADO', propagar(vector3))
  print()
  print('ORIGINAL ', vector4)
  print('PROPAGADO', propagar(vector4))

#%%
if __name__ == '__main__':
  main()
