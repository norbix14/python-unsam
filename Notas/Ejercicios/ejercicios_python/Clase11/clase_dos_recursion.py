#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clase_dos_recursion.py
"""
@author: Norberto Fabrizio
"""

# 11.2 - Intro a la recursion

#%% una funcion recursiva matematica
def factorial_recursivo_simple(n):
  """Calcular el factorial de un numero entero positivo.
  Precondicion: `n` es un entero positivo.
  Devuelve: `n!`
  """
  if n == 1:
    return 1
  return n * factorial_recursivo_simple(n - 1)

#%% 11.1
def factorial_recursivo_debug(n):
  if n == 1:
    r = 1
    return r
  f = factorial_recursivo_debug(n - 1)
  r = n * f
  return r

#%% algoritmos recursivos y algoritmos iterativos
def factorial_iterativo(n):
  f = 1
  for i in range(n, 1, -1):
    f *= i
  return f

#%% un ejemplo de recursion elegante
# de seccion 7.5, ejercicio 7.8
def potencia_iterativa(b, n):
  """Calcular la potencia de `b ^ n`.
  Precondicion: `n >= 0`.
  Devuelve: `b ^ n` mediante un bucle.
  """
  if n <= 0:
    return 1
  r = 1
  for _ in range(n):
    r *= b
  return r
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
def potencia_iterativa_simulando_recursiva(b, n):
  """Calcular la potencia de `b ^ n` simulando una pila de llamadas.
  Precondicion: `n >= 0`.
  Devuelve: `b ^ n`.
  """
  pila = []
  while n > 0:
    if n % 2 == 0:
      pila.append(True)
      n = n // 2
    else:
      pila.append(False)
      n = (n - 1) // 2
  p = 1
  while pila:
    es_par = pila.pop()
    if es_par:
      p *= p
    else:
      p *= p * b
  return p

#%% un ejemplo de recursion poco eficiente
# F(0) = 0
# F(1) = 1
# F(n) = F(n - 1) + F(n - 2) si n > 1
#
def fibonacci_poco_eficiente(n):
  """Calcular la secuencia de Fibonacci.
  Precondicion: `n >= 0`.
  Devuelve: el numero de Fibonacci numero `n`.
  """
  if n == 0:
    res = 0
  elif n == 1:
    res = 1
  else:
    res = fibonacci_poco_eficiente(n - 1) + fibonacci_poco_eficiente(n - 2)
  return res
#
def fibonacci_eficiente_iterando(n):
  """Calcular la secuencia de Fibonacci.
  Precondicion: `n >= 0`.
  Devuelve: el numero de Fibonacci numero `n`.
  """
  if ((n == 0) or (n == 1)):
    return n
  ant2 = 0
  ant1 = 1
  for _ in range(2, n + 1):
    fib = ant1 + ant2
    ant2 = ant1
    ant1 = fib
  return fib
