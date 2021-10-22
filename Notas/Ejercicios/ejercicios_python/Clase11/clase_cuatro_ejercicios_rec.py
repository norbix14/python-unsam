#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clase_cuatro_ejercicios_rec.py
"""
@author: Norberto Fabrizio
"""

# 11.4 - Practica de recursion

#%% Clase07_7.8 - 
#
def sumar_enteros_iterativo(desde, hasta) -> int:
  """Calcular la sumatoria de los números entre `desde` y `hasta`.
  Si `hasta < desde`, entonces devuelve cero.

  Pre: `desde` y `hasta` son números enteros.
  Pos: Se devuelve el valor de sumar todos los números del intervalo
  `[desde, hasta]`. Si el intervalo es vacío se devuelve 0.

  Parametros:
    `desde` (int): desde que numero comenzar a contar.
    `hasta` (int): hasta que numero contar y debe ser mayor a cero.

  Ejemplo:
    >>> sumar_enteros_1(1, 5)
    15

  Ultima actualizacion: 17-09-21 17:00
  """
  if hasta == 0:
    return 0
  suma = 0
  if hasta >= desde:
    for i in range(desde, hasta + 1):
      suma += i
  return suma
#
def sumar_enteros_triangular(desde, hasta) -> int:
  """Calcular la sumatoria de los números entre `desde` y `hasta`.
  Si `hasta < desde`, entonces devuelve cero.

  Pre: `desde` y `hasta` son números enteros.
  Pos: Se devuelve el valor de sumar todos los números del intervalo
  `[desde, hasta]`. Si el intervalo es vacío se devuelve 0.

  Parametros:
    `desde` (int): desde que numero comenzar a contar.
    `hasta` (int): hasta que numero contar y debe ser mayor a cero.

  Ejemplo:
    >>> sumar_enteros_2(1, 5)
    15

  Ultima actualizacion: 18-09-21 12:00
  """
  if hasta == 0:
    return 0
  suma = 0
  if hasta >= desde:
    th = hasta * (hasta + 1) // 2
    td = desde * (desde - 1) // 2
    suma = th - td
  return suma

#%% 11.2 - numeros triangulares
def sumar_enteros_recursivo(desde, hasta) -> int:
  """Calcular la sumatoria de los números entre `desde` y `hasta`.
  Si `hasta < desde`, entonces devuelve cero.

  Pre: `desde` y `hasta` son números enteros.
  Pos: Se devuelve el valor de sumar todos los números del intervalo
  `[desde, hasta]`. Si el intervalo es vacío se devuelve 0.

  Parámetros:
    `desde` (int): desde que número comenzar a contar.
    `hasta` (int): hasta que número contar y debe ser mayor a cero.

  Ejemplo:
    >>> sumar_enteros_1(1, 5)
    15

  Última actualización: 18-10-21 17:30
  """
  if hasta == 0:
    return 0
  def _sumar_enteros(desde: int, hasta: int) -> int:
    """Calcular la sumatoria de los números entre `desde` y `hasta`
    recursivamente.
    """
    suma = 0
    if desde == hasta:
      return hasta
    suma += desde + _sumar_enteros(desde + 1, hasta)
    return suma
  if hasta >= desde:
    return _sumar_enteros(desde, hasta)
  else:
    return 0

#%% 11.3 - digitos
def digitos(n: int) -> int:
  """Contar la cantidad de dígitos que contiene `n`.

  Parámetros:
    `n` (int): digito a contar.

  Ejemplo:
    >>> digitos(123)
    3
  """
  d = str(n) if type(n) is int else n
  if len(d) == 0:
    return 0
  digs = 0
  digs += 1 + digitos(d[1:])
  return digs

#%% 11.4 - potencias
#
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
#
def es_potencia(n, b):
  """Verificar si `n` es potencia de `b`.

  Parámetros:
    `n` (int): potencia.
    `b` (int): base.

  Ejemplo:
    >>> es_potencia(8, 2)
    True
    >>> es_potencia(64, 4)
    True
    >>> es_potencia(70, 10)
    False
    >>> es_potencia(1, 2)
    True
  """
  # TODO: completar
  if n <= 0:
    return 1
  res = False
  return res

#%% 11.5 - subcadenas


#%% 11.6 - paridad


#%% 11.7 - maximo


#%% 11.8 - replicar


#%% 11.9 - pascal
# * ver archivo larenga.py


#%% 11.10 - combinatorios


#%% 11.11 - busqueda binaria
# * ver archivo bbin_rec.py


#%% 11.12 - envolviendo a Fibonacci
# * ver archivo fibonacci_envuelto.py


#%% 11.13 - hojas ISO y recursion
# * ver archivo hojas_ISO.py

