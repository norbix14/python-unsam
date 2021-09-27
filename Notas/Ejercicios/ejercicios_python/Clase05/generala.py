#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# generala.py
"""
@author: Norberto Fabrizio
"""

import random

# 5.2 - Random

#%% calcular probabilidad
def probabilidad(g = 0, n = 0):
  """Calcular y devolver probabilidad.

  Parametros:
    `g` (int): veces que se cumple una condicion.
    `n` (int): veces que se ejecuta una operacion.

  Ejemplo:
    >>> N = 100000
    >>> G = 100
    >>> prob = probabilidad(G, N)
    >>> prob
    0.001000
  """
  g = int(g)
  n = int(n)
  if n == 0:
    return 0.0
  prob = round(g / n, 6)
  return prob

#%% 5.1 - generar valores aleatorios
def tirar(n = 5):
  """Generar una lista con 5 valores enteros aleatorios.

  Parametros:
    `n` (int): cantidad de valores a generar.

  Ejemplo:
    >>> tirar()
    [1, 5, 2, 4, 3]
  """
  n = int(n)
  tirada = []
  if (n > 0) and (n <= 12):
    tirada = [
      random.randint(1, 6)
      for _ in range(n)
    ]
  return tirada

#%% 5.1 - verificar generala servida
def es_generala(tirada = []):
  """Verificar si la tirada es generala servida.

  Parametros:
    `tirada` (list): lista a verificar.

  Ejemplo:
    >>> es_generala([1, 1, 1, 1, 1])
    True
    >>> es_generala([1, 2, 1, 4, 4])
    False
    >>> es_generala(111)
    False
  """
  if ((type(tirada) is not list) or (len(tirada) <= 0)):
    return False
  return min(tirada) == max(tirada)

#%% 5.2 - probabilidad generala servida
def prob_generala(n = 100):
  """Estimar la probabilidad de generala servida en una mano de 3 tiradas.

  Parametros:
    `n` (int): cantidad de simulaciones.

  Ejemplo:
    >>> prob_generala(10000)
    0.0026
    >>> prob_generala('10000')
    0.0026
  """
  if (type(n) is str):
    n = int(n)
  if (type(n) is not int):
    return 0.0
  generalas = 0
  for _ in range(n):
    mano = tirar()
    if (es_generala(mano)):
      generalas += 1
    else:
      val = mano[0]
      for _ in range(2):
        mano = [val] + tirar(4)
        if (es_generala(mano)):
          generalas += 1
  return generalas / n
