#!/usr/bin/env python3
# invlista.py

######################################################################
"""
@author: Norberto Fabrizio
"""

# 4.5

#%% definicion de la funcion
def invertir_lista(lista = []):
  """Mostrar la lista invertida.

  Parametros:
    `lista` (list): lista de elementos.

  Ejemplo:
    >>> lista1 = [1,2,3,4,5]
    >>> lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
    >>> print(invertir_lista(lista1))
    [5,4,3,2,1]
    >>> print(invertir_lista(lista2))
    ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
    >>> print(invertir_lista([]))
    []
  """
  if (type(lista) is list):
    if (len(lista) <= 0):
      return []
    invertida = []
    i = len(lista) - 1
    for e in lista:
      invertida.append(lista[i])
      i -= 1
    return invertida
  return lista

#%% test
if __name__ == '__main__':
  lista1 = [1, 2, 3, 4, 5]
  lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
  print('ORIGINAL: ', lista1)
  print('INVERTIDO:', invertir_lista(lista1))
  print()
  print('ORIGINAL: ', lista2)
  print('INVERTIDO:', invertir_lista(lista2))
