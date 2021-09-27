#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# invlista.py
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
    >>> invertir_lista([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
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

#%%
def main():
  """Main. Ejecutar algunas pruebas."""
  lista1 = [1, 2, 3, 4, 5]
  lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
  print('ORIGINAL: ', lista1)
  print('INVERTIDO:', invertir_lista(lista1))
  print()
  print('ORIGINAL: ', lista2)
  print('INVERTIDO:', invertir_lista(lista2))

#%%
if __name__ == '__main__':
  main()
