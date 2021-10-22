#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bbin_rec.py
"""
@author: Norberto Fabrizio
"""

# 11.4 - Practica de recursion

#%% 11.11 - 
def bbinaria_rec(lista, e) -> bool:
  """Buscar un elemento `e` en `lista` de manera recursiva y devolver
  `True` o `False` si este se encuentra.

  Parámetros:
    `lista` (lista): listado de elementos que deben estar ordenados.
    `e` (any): elemento a buscar.

  Ejemplo:
    >>> bbinaria_rec([0, 2, 3, 5, 6, 8, 9, 14], 8)
    True
    >>> bbinaria_rec([0, 2, 3, 5, 6, 8, 9, 14], 15)
    False

  Última actualización: 21-10-2021 10:00
  """
  if len(lista) == 0:
    res = False
  elif len(lista) == 1:
    res = lista[0] == e
  else:
    medio = len(lista) // 2
    if lista[medio] >= e:
      if lista[medio] == e:
        return True
      res = bbinaria_rec(lista[:medio], e)
    else:
      res = bbinaria_rec(lista[medio:], e)
  return res
