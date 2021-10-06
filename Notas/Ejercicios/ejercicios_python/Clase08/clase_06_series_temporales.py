#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clase_06_series_temporales.py
"""
@author: Norberto Fabrizio
"""

import os

import numpy as np

import pandas as pd

from scipy.stats import pearsonr

import matplotlib.pyplot as plt

# 8.6 - Series temporales

#%% leer archivo csv de series
def leer_archivo(fname):
  """Leer archivo CSV y devolver un DataFrame.

  Parametros:
    `fname` (str): archivo csv.

  Última actualización: 05-10-2021 14:30
  """
  return pd.read_csv(fname, low_memory=False, index_col=['Time'], parse_dates=True)

#%% crear copia de pedazos a eleccion
def crear_copia(df, start=None, end=None):
  """Crear una copia.

  Parametros:
    `df` (DataFrame): dataframe principal.
    `start` (str): fecha desde donde comenzar a contar.
    `end` (str): fecha hasta donde contar.

  Última actualización: 05-10-2021 15:30
  """
  return df[start:end].copy()

#%% 8.10
# ver archivo mareas_a_mano.py

#%% correlacion con desplazamientos
def correlacion_desplazamientos(df):
  """Calcular y graficar el coeficiente de correlacion r de Pearson.
  
  Parametros:
    `df` (DataFrame): dataframe con los datos.

  Última actualización: 05-10-2021 18:30
  """
  dh = crear_copia(df, start='10-01-2014')
  shifts = np.arange(-12, 13)
  corrs = np.zeros(shifts.shape)
  for i, sh in enumerate(shifts):
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[12:-12], dh['H_BA'][12:-12])[0] 
  plt.plot(shifts, corrs)

#%% 8.11 - interpolacion
def interpolacion(df):
  """Interpolar la serie de manera de poder usar desplazamientos menores
  a una hora.

  Parametros:
    `df` (DataFrame): dataframe con los datos.

  Última actualización: 05-10-2021 18:30
  """
  dh = crear_copia(df, start='10-01-2014')
  freq_horaria = 4 # 4 para 15 minutos, 60 para 1 minutos
  cant_horas = 24
  N = cant_horas * freq_horaria
  # hacer resample cada tantos minutos
  dh = dh.resample(f'{int(60 / freq_horaria)}T').mean()
  # rellenar NaNs suavemente
  dh = dh.interpolate(method='quadratic')
  # generar vector de desplazamientos (enteros)
  ishifts = np.arange(-N, N + 1)
  # y su desplazamiento horario asociado
  shifts = ishifts / freq_horaria
  # finalmente calculo las correlaciones correspondientes
  corrs = np.zeros(shifts.shape)
  for i, sh in enumerate(ishifts):
      corrs[i] = pearsonr(dh['H_SF'].shift(sh)[N: -N], dh['H_BA'][N: -N])[0]
  # y grafico
  plt.plot(shifts, corrs)

#%% optativos
# analisis por medio de transformadas de Fourier
# espectro de potencia y de angulos para san fernando
# espectro de potencia y de angulos para buenos aires
# ejercicio 8.12 - desfasajes
# ejercicio 8.13 - otros puertos
# ejercicio 8.14 - otros periodos
# archivo a crear: mareas_fft.py

#%%
if __name__ == '__main__':
  directorio = '../Data'
  series_csv = 'OBS_SHN_SF-BA.csv'

  fname_series_temporales = os.path.join(directorio, series_csv)

  df = leer_archivo(fname_series_temporales)
