#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# random_walk.py
"""
@author: Norberto Fabrizio
"""

import sys

import numpy as np

from matplotlib import pyplot as plt

# 7.7 - La biblioteca matplotlib

#%% 7.11 - 
def subplots_fuera_grilla(n = 0):
  plt.figure()

  plt.subplot(2, 1, 1)
  plt.plot([0,1,2],[0,1,0])
  plt.xticks([]), plt.yticks([])

  plt.subplot(2, 3, 4)
  plt.plot([0,1],[0,1])
  plt.xticks([]), plt.yticks([])

  plt.subplot(2, 3, 5)
  plt.plot([0,1],[1,1])
  plt.xticks([]), plt.yticks([])

  plt.subplot(2, 3, 6)
  plt.plot([0,1],[1,0])
  plt.xticks([]), plt.yticks([])

  plt.show()

#%% 7.12 - 
# 
def randomwalk(largo = 100):
  """Realizar sucesivos pasos aleatorios.

  Parametros:
    `largo` (int): cantidad de pasos.

  Ejemplo:
    >>> randomwalk(10)
    array([-1, -2, -1, -1, -2, -1, -1, -1, -1, -1])

  Ultima actualizacion: 20-09-21 15:00
  """
  pasos = np.random.randint(-1, 2, largo)
  return pasos.cumsum()
# 
def graficar_randomwalk(n = 100000):
  """Graficar randomwalk.

  Parametros:
    `n` (int): pasos.

  Ejemplo:
    >>> graficar_randomwalk(100000)
    # muestra el grafico

  Ultima actualizacion: 20-09-21 22:00
  """
  colors = [
    'black','maroon','brown','red','tomato',
    'orange','green','darkcyan','royalblue',
    'navy','indigo','crimson'
  ]
  randomwalks = [randomwalk(n) for _ in range(12)]
  recorridos = [(max(map(abs, walks)), walks) for walks in randomwalks]
  rec_mas_alejado = max(recorridos)[1]
  rec_menos_alejado = min(recorridos)[1]

  plt.figure(figsize=(10, 6), dpi=80)

  plt.subplot(2,1,1)
  for i in range(12):
    plt.plot(randomwalks[i], color=colors[i], linewidth=0.88)
  plt.xticks([])
  plt.title('12 caminatas al azar')

  plt.subplot(2,2,3)
  plt.plot(rec_mas_alejado)
  plt.xticks([])
  plt.title('La caminata que mas se aleja')

  plt.subplot(2,2,4)
  plt.plot(rec_menos_alejado)
  plt.xticks([])
  plt.title('La caminata que menos se aleja')

  plt.show()

# optativos

#%% 7.13 - 

#%% 7.14 - 

#%% 7.15 - 

#%% main
def main():
  """Funcion principal."""
  args = sys.argv
  if (len(args) <= 1):
    print('---- Modo de uso ----')
    print(f'{args[0]} [a]')
    print('----')
    print('Parametro [a]: pasos a generar.')
    print(f'EJEMPLO: {args[0]} 100000')
  else:
    n = int(args[1])
    graficar_randomwalk(n)

#%%
if __name__ == '__main__':
  main()
