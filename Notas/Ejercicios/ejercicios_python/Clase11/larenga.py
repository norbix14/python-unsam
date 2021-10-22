#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# larenga.py
"""
@author: Norberto Fabrizio
"""

# 11.4 - Práctica de recursión

# TODO: completar

#%% guía - 
# * https://solocodigoweb.com/blog/2014/04/16/triangulo-de-pascal-en-python/
def triangulo_pascal(rows):
  """Función que recibe como parámetro el número de filas del triángulo."""
  #si el número de filas es cero devolvemos vacío.
  if rows == 0:
    return []
  #si el número de filas es 1, devolvemos triángulo con una sola fila.
  elif rows == 1:
    return [[1]]
  else:
    #de lo contrario armamos el triángulo según el número de filas
    new_row = [1]
    #llamamos nuevamente a la función para armar el triángulo
    result = triangulo_pascal(rows - 1)
    #guardamos la última fila.
    last_row = result[-1]
    #iteramos la cantidad de veces del valor de filas - 1.
    for i in range(len(last_row) - 1):
      #agregamos los valores a la nueva fila.
      new_row.append(last_row[i] + last_row[i + 1])
    new_row += [1]
    #agregamos a la matriz del triángulo la nueva fila
    result.append(new_row)
  #devolvemos el array con los valores del triángulo.
  return result

#%% 11.9 - pascal
def pascal(n, k):
  """Calcular el valor que se encuentra en la fila `n` y la columna
  `k`.

  Parámetros:
    `n` (): 
    `k` (): 
  """
  return 0
