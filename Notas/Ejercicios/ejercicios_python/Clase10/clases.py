#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clases.py
"""
@author: Norberto Fabrizio
"""

import os

#%% 10.2 - El protocolo de iteracion
# iterable
class Camion():
  def __init__(self) -> None:
    self.lotes = []

  def __iter__(self):
    return self.lotes.__iter__()
# 10.1 - iteradores, un ejemplo
def ej_101():
  a = [1, 9, 4, 25, 16]
  iter = a.__iter__()
  return iter

#%% 10.3 - Iteracion a medida
#
def regresiva(n):
  while n > 0:
    yield n
    n -= 1
#
def filematch(filename, substr):
  with open(filename, 'rt', encoding='UTF-8') as f:
    for line in f:
      if substr in line:
        yield line

#%% 10.4 - Productores, consumidores y cañerias
# productor
def productor(filename):
  with open(filename, 'rt', encoding='UTF-8') as f:
    for linea in f:
      yield linea
#
def procesamiento(elemento):
  next(elemento)
  for el in elemento:
    yield el
#
def consumidor(producto):
  for item in producto:
    print(item)

#%% 10.5 - Mas sobre generadores
#
def generador_pares(lista):
  return (l * 2 for l in lista if l % 2 == 0)
# 10.13
def generador_cuadrados(nums):
  return (n * n for n in nums)
# 10.14
def generador_suma(nums):
  return sum(n for n in nums)

#%%
if __name__ == '__main__':
  dir = 'Data'
  camion_csv = 'camion.csv'
  camion_ruta = os.path.join('..', dir, camion_csv)
  # iterable
  camion = Camion()
  # 10.1
  iter = ej_101()
  # expresiones generadoras
  nums = [1,2,3,4,5,6,7,8,9]
  gp = generador_pares(nums)
  cuadrados = generador_cuadrados(nums)
  suma = generador_suma(nums)
