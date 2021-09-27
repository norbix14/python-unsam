#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# plotear_temperaturas.py
"""
@author: Norberto Fabrizio
"""

import numpy as np

import matplotlib.pyplot as plt

# 5.9 - Empezando a plotear.

#%% 5.9 - empezando a plotear
def plotear_temperaturas(nombre_archivo = '../Data/temperaturas.npy'):
  """Plotear las temperaturas medidas.

  Parametros:
    `nombre_archivo` (str): archivo donde buscar las temperaturas.

  Ejemplo:
    >>> plotear_temperaturas('../Data/temperaturas.npy')
    # mostrar el histograma
  """
  try:
    temperaturas = np.load(nombre_archivo)
    plt.hist(temperaturas, bins=100)
    plt.xlabel('Temperaturas')
    plt.ylabel('Probabilidad')
    plt.title('Mediciones de temperaturas')
    plt.show()
  except FileNotFoundError:
    return f'No existe el archivo "{nombre_archivo}".'
