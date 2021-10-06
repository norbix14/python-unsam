#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clase_08_pandas.py
"""
@author: Norberto Fabrizio
"""

import os

import pandas as pd

import seaborn as sns

# 8.5 - Introducción a Pandas

#%% lectura de datos
def lectura_datos(fname):
  """Leer archivo csv con Pandas.

  Parametros:
    `fname` (str): directorio donde buscar datos.
  """
  return pd.read_csv(fname, low_memory=False)

#%% series temporales en pandas

#%% incorporando el arbolado lineal

#%% 8.7 - lectura y seleccion
# cantidad de todas las especies
def lectura_seleccion_uno(df_lineal):
  """Mostrar las 10 especies mas frecuentes y sus cantidades.

  Parametros:
    `df_lineal` (any): dataframe con los datos del arbolado.
  """
  cols_sel = [
    'nombre_cientifico', 'ancho_acera',
    'diametro_altura_pecho', 'altura_arbol'
  ]
  df_lineal = df_lineal[cols_sel]
  return df_lineal[cols_sel[0]].value_counts().head(10)
# cantidad de especies seleccionadas
def lectura_seleccion_dos(df_lineal):
  """Mostrar las especies seleccionadas y sus cantidades.

  Parametros:
    `df_lineal` (any): dataframe con los datos del arbolado.
  """
  cols_sel = [
    'nombre_cientifico', 'ancho_acera',
    'diametro_altura_pecho', 'altura_arbol'
  ]
  especies_seleccionadas = [
    'Tilia x moltkei',
    'Jacaranda mimosifolia',
    'Tipuana tipu'
  ]
  df_lineal = df_lineal[cols_sel]
  df_lineal_seleccion = df_lineal[
    df_lineal[cols_sel[0]].isin(especies_seleccionadas)
  ]
  return df_lineal_seleccion[cols_sel[0]].value_counts()
# datos seleccionados de especies seleccionadas
def lectura_seleccion_tres(df_lineal):
  """Mostrar las especies seleccionadas.

  Parametros:
    `df_lineal` (any): dataframe con los datos del arbolado.
  """
  cols_sel = [
    'nombre_cientifico', 'ancho_acera',
    'diametro_altura_pecho', 'altura_arbol'
  ]
  especies_seleccionadas = [
    'Tilia x moltkei',
    'Jacaranda mimosifolia',
    'Tipuana tipu'
  ]
  df_lineal = df_lineal[cols_sel]
  df_lineal_seleccion = df_lineal[
    df_lineal[cols_sel[0]].isin(especies_seleccionadas)
  ]
  return df_lineal_seleccion

#%% 8.8 - boxplots
# diametros de los arboles
def boxplot_uno(df_lineal):
  """Mostrar boxplot de diametros."""
  df_lineal.boxplot('diametro_altura_pecho', by='nombre_cientifico')
# alturas de los arboles
def boxplot_dos(df_lineal):
  """Mostrar boxplot de alturas."""
  df_lineal.boxplot('altura_arbol', by='nombre_cientifico')
# pairplot
def pairplot_uno(df_lineal):
  """Mostrar pairplot de un dataframe."""
  sns.pairplot(data=df_lineal, hue='nombre_cientifico')

#%% 8.9 - comparando especies en parques y en veredas
# ver archivo arbolado_parques_veredas.py

#%%
if __name__ == '__main__':
  directorio = '../Data'
  archivo_arbolado_verdes = 'arbolado-en-espacios-verdes.csv'
  archivo_arbolado_publico = 'arbolado-publico-lineal-2017-2018.csv'

  fname_arbolado_verdes = os.path.join(directorio, archivo_arbolado_verdes)
  fname_arbolado_lineal = os.path.join(directorio, archivo_arbolado_publico)

  df_parque = lectura_datos(fname_arbolado_verdes)
  df_lineal = lectura_datos(fname_arbolado_lineal)
