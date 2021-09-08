#!/usr/bin/env python3
# termometro.py

import random
import numpy as np

######################################################################
"""
@author: Norberto Fabrizio
"""

# 5.6 - Gaussiana

#%% 5.6 y 5.8 - realizar n mediciones de temperatura y guardarlas
def medir_temp(n = 999, ubicacion = '../Data/temperaturas'):
  """Simular mediciones de temperatura.

  Parametros:
    `n` (int): cuantas mediciones realizar.
    `ubicacion` (str): donde guardar las mediciones.

  Ejemplo:
    >>> from pprint import pprint
    >>> pprint(medir_temp())
    # 999 mediciones por defecto
    # se muestran 10 a modo de ejemplo
    [37.58436819257656,
     37.01738443488977,
     37.26033946627048,
     36.89382661883949,
     37.781819074216216,
     37.574205196507755,
     37.21966409806708,
     37.156513771303736,
     37.33566077442359,
     37.446282095243]
    >>> pprint(medir_temp(n = 100, ubicacion = '../Data/temperaturas'))
    # se muestran 10 a modo de ejemplo
    # las mediciones se guardaran en la carpeta `Data`
    # se creara un archivo `temperaturas.npy` con datos para el ploteo
    [37.58436819257656,
     37.01738443488977,
     37.26033946627048,
     36.89382661883949,
     37.781819074216216,
     37.574205196507755,
     37.21966409806708,
     37.156513771303736,
     37.33566077442359,
     37.446282095243]
  """
  n = int(n)
  temp_real = 37.5
  m = [
    random.normalvariate(mu=0.0, sigma=0.2) + temp_real
    for _ in range(n)
  ]
  try:
    np.save(ubicacion, m)
  except FileNotFoundError:
    msg = f'No se pudieron guardar los datos en "{ubicacion}"'
    pass
  return m

#%% 5.6 - resumen de mediciones de temperatura
def resumen_temp(n = 999):
  """Calcular el maximo, minimo, promedio y mediana de
  las mediciones realizadas.

  Parametros:
    `n` (int): simulaciones a realizar.

  Ejemplo:
    >>> print(resumen_temp())
    # mediciones en 999 simulaciones por defecto
    (38.18, 36.86, 37.49, 37.5)
    >>> print(resumen_temp(100))
    (38.0, 37.07, 37.48, 37.56)
    >>> print(resumen_temp(101))
    (38.03, 36.91, 37.48, 37.48)
  """
  n = int(n)
  temps = medir_temp(n)
  maximo = round(max(temps), 2)
  minimo = round(min(temps), 2)
  promedio = round(sum(temps) / len(temps), 2)
  mediana = 0
  mitad = len(temps) // 2
  if (len(temps) % 2 == 0):
    mediana = round((temps[mitad - 1] + temps[mitad]) / 2, 2)
  else:
    temps.sort()
    mediana = round(temps[mitad], 2)
  return (maximo, minimo, promedio, mediana)
