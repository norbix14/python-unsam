#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# documentacion.py

###############################################################################

# 7.5 - Contratos: especificacion y documentacion

#%% 7.8 - 
# implementacion con ciclo
def sumar_enteros_1(desde, hasta):
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
# implementacion sin ciclo
def sumar_enteros_2(desde, hasta):
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

#%% 7.10 - 
#
def valor_absoluto(n):
  """Devolver el valor absoluto de un numero.

  Parametros:
    `n` (int): numero.

  Ejemplo:
    >>> valor_absoluto(0)
    0
    >>> valor_absoluto(10)
    10
    >>> valor_absoluto(-10)
    10

  Ultima actualizacion: 17-09-21 16:16
  """
  if n >= 0:
    return n
  else:
    return - n
#
def suma_pares(l):
  """Devolver la suma de todos los pares dentro de una lista.

  Parametros:
    `l` (list): listado de enteros positivos.

  Ejemplo:
    >>> suma_pares([1,2,3,4,5,6,7,8,9])
    20

  Ultima actualizacion: 17-09-21 16:16
  """
  res = 0
  for e in l:
    if e % 2 == 0:
      res += e
    else:
      res += 0
  return res
#
def veces(a, b):
  """Repetir `b` veces `a` y obtener el resultado sumandolos.

  Parametros:
    `a` (int): entero a repetir.
    `b` (int): cantidad de repeticiones.

  Ejemplo:
    >>> veces(3, 5)
    15

  Ultima actualizacion: 17-09-21 16:16
  """
  res = 0
  nb = b
  while nb != 0:
    #print(nb * a + res)
    res += a
    nb -= 1
  return res
#
def collatz(n):
  """Conjetura de Collatz.

  Aplicar operaciones matematicas a un numero entero positivo.
  Si `n` es par se divide por 2 y si es impar, se multiplica por 3
  y al resultado se le suma 1. Al final, se retornara cuantas
  operaciones se realizaron sobre `n`.

  Parametros:
    `n` (int): entero positivo sobre el cual aplicar las operaciones.

  Ejemplo:
    >>> collatz(100)
    26
    >>> collatz(103)
    88

  Ultima actualizacion: 17-09-21 16:16
  """
  res = 1
  while n != 1:
    if n % 2 == 0:
      n = n // 2
    else:
      n = 3 * n + 1
    res += 1
  return res
