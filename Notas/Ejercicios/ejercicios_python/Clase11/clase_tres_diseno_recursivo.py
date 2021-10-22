#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clase_tres_diseno_recursivo.py
"""
@author: Norberto Fabrizio
"""

# 11.3 - Diseño de algoritmos recursivos

#%% un primer diseño recursivo
def sumar_recursivo(lista):
  """Sumar todos los numeros de la `lista`.
  Precondicion: longitud (`len(lista) >= 1`) de la lista mayor a 1.
  Devuelve: la suma de todos los numeros.

  Parametros:
    `lista` (list[int]): listado de enteros positivos.

  Ejemplo:
    >>> sumar([1,2,3,4,5,6,7,8,9])
    45
  """
  res = 0
  if len(lista) != 0:
    res = lista[0] + sumar_recursivo(lista[1:])
  return res

#%% recursion de cola
#
def sumar_recursivo_cola(lista, suma = 0):
  """Sumar todos los numeros de la `lista`.
  Precondicion: longitud (`len(lista) >= 1`) de la lista mayor a 1.
  Devuelve: la suma de todos los numeros.

  Parametros:
    `lista` (list[int]): listado de enteros positivos.

  Ejemplo:
    >>> sumar([1,2,3,4,5,6,7,8,9])
    45
  """
  res = suma
  if len(lista) != 0:
    res = sumar_recursivo_cola(lista[1:], lista[0] + suma)
  return res
#
def sumar_iterativo(lista):
  """Sumar todos los numeros de la `lista`.
  Precondicion: longitud (`len(lista) >= 1`) de la lista mayor a 1.
  Devuelve: la suma de todos los numeros.

  Parametros:
    `lista` (list[int]): listado de enteros positivos.

  Ejemplo:
    >>> sumar([1,2,3,4,5,6,7,8,9])
    45
  """
  suma = 0
  while lista:
    lista, suma = lista[1:], lista[0] + suma
  return suma

#%% modificacion de la firma
#
def promediar(lista):
  """Calcular el promedio de la lista.

  Parametros:
    `lista` (list): listado de elementos.
  """
  def promediar_recursivo(lista):
    """Calcular la suma de la cantidad de elementos y su cantidad en la lista.

    Parametros:
      `lista` (list): listado de elementos.
    """
    suma = lista[0]
    cantidad = 1
    if len(lista) > 1:
      suma_resto, cantidad_resto = promediar_recursivo(lista[1:])
      suma += suma_resto
      cantidad += cantidad_resto
    return suma, cantidad

  suma, cantidad = promediar_recursivo(lista)
  return suma / cantidad
# funcion wrapper
def potencia(b, n):
  """Calcular la potencia de `b ^ n`."""
  if n < 0:
    b = 1 / b
    n = -n
  def potencia_recursiva(b, n):
    """Calcular la potencia de `b ^ n`.
    Precondicion: `n >= 0`.
    Devuelve: `b ^ n` de forma recursiva.
    """
    #### caso base
    # si n <= 0 entonces devuelve 1
    #### si n es par
    # b ^ n = b ^ (n / 2) * b ^ (n / 2)
    #### si es impar
    # b ^ n = b ^ ((n - 1) / 2) * b ^ ((n - 1) / 2)
    if n <= 0:
      return 1
    if n % 2 == 0:
      p = potencia_recursiva(b, n // 2)
      return p * p
    else:
      p = potencia_recursiva(b, (n - 1) // 2)
      return p * p * b
  return potencia_recursiva(b, n)

if __name__ == '__main__':
  lista = [1,2,3,4,5,6,7,8,9]
