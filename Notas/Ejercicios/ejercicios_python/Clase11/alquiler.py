#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# alquiler.py
"""
@author: Norberto Fabrizio
"""

# 11.5 - Regresión lineal

import numpy as np

# TODO: completar

#%% 11.14 - precio_alquiler ~ superficie
#
def ajuste_lineal_simple(x, y):
  a = sum(((x - x.mean()) * (y - y.mean()))) / sum(((x - x.mean()) ** 2))
  b = y.mean() - a * x.mean()
  return a, b
#
def precio_alquiler():
  """Modelar el precio de alquiler a partir de la superficie."""
  superficie = np.array([150.0, 120.0, 170.0, 80.0])
  alquiler = np.array([35.0, 29.6, 37.4, 21.0])
  a, b = ajuste_lineal_simple(superficie, alquiler)
  errores = alquiler - (a * superficie + b)
  print(errores)
  print("ECM:", (errores ** 2).mean())
  return 0
