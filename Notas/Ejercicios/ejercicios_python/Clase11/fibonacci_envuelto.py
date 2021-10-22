#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# fibonacci_envuelto.py
"""
@author: Norberto Fabrizio
"""

# 11.4 - Practica de recursion

# TODO: completar

#%% 11.12 - 
def fibonacci(n):
  """Obtener un entero positivo `n` y devolver el n-ésimo número de `Fibonacci`
  donde `F(0) = 0 y F(1) = 1`.

  Parámetros:
    `n` (int): enésimo número de Fibonacci.

  Ejemplo:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1

  Última actualización: 22-10-2021 09:30
  """
  def fibonacci_aux(n, dict_fibo):
    """Calcular el n-ésimo número de Fibonacci de forma recursiva utilizando
    un diccionario para almacenar los valores ya computados.
    `dict_fibo` es un diccionario que guarda en la clave `k` el valor de `F(k)`.
    """
    if n in dict_fibo.keys():
      F = dict_fibo[n]
    else:
      # ! completar
      print(n)
      dict_fibo[n] = 1 + 2
      #dict_fibo[n] = dict_fibo[n + 1] + dict_fibo[n + 2]
      F, dict_fibo = fibonacci_aux(n - 1, dict_fibo)

    # ! completar
    print(dict_fibo)
    return F, dict_fibo

  #! no modificar
  dict_fibo = {0:0, 1:1} 
  F, dict_fibo = fibonacci_aux(n, dict_fibo)
  return F
