#!/usr/bin/env python3
# estimar_pi.py

import random

######################################################################
"""
@author: Norberto Fabrizio
"""

# 5.5 - Calcular PI

#%% generar puntos aleatorios
def generar_punto():
  """Generar aleatoriamente punto `x` e `y`."""
  x = random.random()
  y = random.random()
  return x, y

#%% estimar pi
def estimar_pi(n):
  """Generar 100000 puntos aleatorios y estimar `PI`."""
  return 0

#%% distribucion normal o Gaussiana
def gaussiana(n = 10):
  """Generar distribucion Gaussiana."""
  g = [
    round(random.normalvariate(mu=0, sigma=1), 2)
    for _ in range(n)
  ]
  return g
