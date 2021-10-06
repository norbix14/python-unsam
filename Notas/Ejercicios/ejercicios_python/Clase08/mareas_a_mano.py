#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mareas_a_mano.py
"""
@author: Norberto Fabrizio
"""

import os

import pandas as pd

# 8.6 - Series temporales
# 8.10

#%% leer archivo csv de series
def leer_archivo(fname):
  """Leer archivo CSV y devolver un DataFrame.

  Parametros:
    `fname` (str): archivo csv con los datos temporales.

  Ejemplo:
    >>> leer_archivo('../Data/OBS_SHN_SF-BA.csv')
    # devuelve un DataFrame

  Última actualización: 05-10-2021 19:00
  """
  try:
    return pd.read_csv(fname, low_memory=False, index_col=['Time'], parse_dates=True)
  except FileNotFoundError as e:
    print(f'Error: {e}')
    return pd.DataFrame([])

#%% crear copia de pedazos a eleccion
def crear_copia(df, start=None, end=None):
  """Crear una copia del DataFrame principal.

  Parametros:
    `df` (DataFrame): dataframe principal.
    `start` (str): fecha desde donde comenzar a contar.
    `end` (str): fecha hasta donde contar.

  Ejemplo:
    >>> df = leer_archivo('../Data/OBS_SHN_SF-BA.csv')
    >>> crear_copia(df, start='12-1-2014', end='12-25-2014')
    # devuelve una copia del DataFrame principal

  Última actualización: 05-10-2021 19:00
  """
  return df[start:end].copy()

#%% unir series y graficarlas
def unir_series_graficar(dh, delta_t=0, delta_h=0.0):
  """Unir dos series y graficar mediante un plot.

  Parametros:
    `dh` (DataFrame): dataframe.
    `delta_t` (int): es un numero entero y son pasos.
    `delta_h` (float): es un numero flotante.

  Ejemplo:
    >>> df = leer_archivo('../Data/OBS_SHN_SF-BA.csv')
    >>> dh = crear_copia(df, start='12-1-2014', end='12-25-2014')
    >>> unir_series_graficar(dh)
    # muestra un plot

  Última actualización: 05-10-2021 19:00
  """
  pd.DataFrame([
    dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']
  ]).T.plot()

#%%
def main():
  """Main. Ejecutar todas las funciones."""
  directorio = '../Data'
  archivo = 'OBS_SHN_SF-BA.csv'
  fname = os.path.join(directorio, archivo)

  df = leer_archivo(fname)

  dh = crear_copia(df, start='12-25-2014')

  unir_series_graficar(dh)

  unir_series_graficar(dh, -1, 18.0)

#%%
if __name__ == '__main__':
  main()
