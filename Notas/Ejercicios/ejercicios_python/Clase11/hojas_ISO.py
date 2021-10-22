#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# hojas_ISO.py
"""
@author: Norberto Fabrizio
"""

# 11.4 - Practica de recursion

#%% 11.13 - 
def medidas_hoja_A(n = 0) -> tuple:
  """Calcular el ancho y el largo de una hoja `A(n)`.
  Se devolverá una tupla con las medidas del ancho y largo en milímetros.

  Parámetros:
    `n` (int): tamaño de hoja.

  Ejemplo:
    >>> medidas_hoja_A(0)
    (841, 1189)
    >>> medidas_hoja_A(1)
    (594, 841)
    >>> medidas_hoja_A(2)
    (420, 594)
    >>> medidas_hoja_A(3)
    (297, 420)
    >>> medidas_hoja_A(4)
    (210, 297)
    >>> medidas_hoja_A(10)
    (26, 37)

  Última actualización: 22-10-2021 15:30
  """
  ancho_a0 = 841
  largo_a0 = 1189
  if n <= 0:
    return (ancho_a0, largo_a0)
  a, l = medidas_hoja_A(n - 1)
  return (l // 2, a)
