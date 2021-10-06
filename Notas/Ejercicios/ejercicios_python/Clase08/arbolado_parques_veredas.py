#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# arbolado_parques_veredas.py
"""
@author: Norberto Fabrizio
"""

import os

import pandas as pd

# 8.5 - Introduccion a Pandas
# 8.9 - Comparando especies en parques y en veredas

#%% 1 - datasets
# dataset de arbolado en espacios verdes
def parques(fname):
  """Generar dataset del arbolado en parques.

  Parametros:
    `fname` (str): ruta al archivo csv.

  Ejemplo:
    >>> parques('../Data/arbolado-en-espacios-verdes.csv')
    # devuelve un DataFrame con los datos del arbolado

  Última actualización: 05-10-2021 19:00
  """
  return pd.read_csv(fname, low_memory=False)
# dataset de arbolado en veredas
def veredas(fname):
  """Generar dataset del arbolado en veredas.

  Parametros:
    `fname` (str): ruta al archivo csv.

  Ejemplo:
    >>> veredas('../Data/arbolado-publico-lineal-2017-2018.csv')
    # devuelve un DataFrame con los datos del arbolado

  Última actualización: 05-10-2021 19:00
  """
  return pd.read_csv(fname, low_memory=False)

#%% 2 - datasets solo de tipas
# tipas en espacios verdes
def tipas_parques(df):
  """Mostrar una copia del DataFrame principal pero solamente de tipas en
  espacios verdes.

  Parametros:
    `df` (DataFrame): todos los datos del arbolado.  

  Ejemplo:
    >>> df = parques('../Data/arbolado-en-espacios-verdes.csv')
    >>> tipas_parques(df)
    # devuelve una copia del DataFrame principal con los datos del arbolado

  Última actualización: 05-10-2021 19:00
  """
  especie = 'tipuana tipu'
  cols = ['altura_tot', 'diametro', 'nombre_cie']

  df_copy = df[cols].copy()

  to_lower = df_copy['nombre_cie'].transform(lambda s: s.lower())
  df_copy['nombre_cie'] = to_lower

  df_tipa = df_copy[df_copy['nombre_cie'] == especie]

  df_tipa = df_tipa.rename(columns={
    'altura_tot': 'altura_arbol',
    'diametro': 'diametro_altura_pecho',
    'nombre_cie': 'nombre_cientifico'
  })
  df_tipa.loc[:, 'ambiente'] = 'parque'

  return df_tipa
# tipas en veredas
def tipas_veredas(df):
  """Mostrar una copia del DataFrame principal pero solamente de tipas en
  veredas.

  Parametros:
    `df` (DataFrame): todos los datos del arbolado.  

  Ejemplo:
    >>> df = veredas('../Data/arbolado-publico-lineal-2017-2018.csv')
    >>> tipas_veredas(df)
    # devuelve una copia del DataFrame principal con los datos del arbolado

  Última actualización: 05-10-2021 19:00
  """
  especie = 'tipuana tipu'
  cols = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']

  df_copy = df[cols].copy()

  to_lower = df_copy['nombre_cientifico'].transform(lambda s: s.lower())
  df_copy['nombre_cientifico'] = to_lower

  df_tipa = df_copy[df_copy['nombre_cientifico'] == especie]
  df_tipa.loc[:, 'ambiente'] = 'vereda'

  return df_tipa

#%% dataset generico
def especie_generica(df, especie, key, ambiente, cols):
  """Mostrar dataframe de alguna especie.

  Parametros:
    `df` (DataFrame): todos los datos del arbolado.
    `especie` (str): especie a mostrar en el dataset.
    `key` (str): clave a filtrar (que columna).
    `ambiente` (str): ambiente al que pertenece la especie.
    `cols` (list): columnas a mostrar.

  Ejemplo:
    >>> df = veredas('../Data/arbolado-publico-lineal-2017-2018.csv')
    >>> cols = ['nombre_cientifico', 'altura_arbol', 'diametro_altura_pecho']
    >>> especie_generica(df, 'tipuana tipu', 'nombre_cientifico', 'vereda', cols)
    # devuelve una copia del DataFrame principal con los datos del arbolado

  Última actualización: 05-10-2021 19:00
  """
  especie = especie.lower()
  key = key.lower()
  ambiente = ambiente.lower()

  df_copy = df[cols].copy()

  to_lower = df_copy[key].transform(lambda s: s.lower())
  df_copy[key] = to_lower

  df_generico = df_copy[df_copy[key] == especie]
  df_generico.loc[:, 'ambiente'] = ambiente

  return df_generico

#%% 3 - agregar ambientes

#%% 4 - juntar datasets
def juntar_datasets(df_tipas_parques, df_tipas_veredas):
  """Fusionar dos datasets.

  Parametros:
    `df_tipas_parques` (DataFrame): dataset de tipas en parques.
    `df_tipas_veredas` (DataFrame): dataset de tipas en veredas.

  Ejemplo:
    >>> df_parques = parques('../Data/arbolado-en-espacios-verdes.csv')
    >>> df_tipas_parques = tipas_parques(df_parques)

    >>> df_veredas = veredas('../Data/arbolado-publico-lineal-2017-2018.csv')
    >>> df_tipas_veredas = tipas_veredas(df_veredas)

    >>> juntar_datasets(df_tipas_parques, df_tipas_veredas)
    # fusiona los dos datasets para poder plotear luego

  Última actualización: 05-10-2021 19:00
  """
  return pd.concat([df_tipas_parques, df_tipas_veredas])

#%% 5 - crear boxplots
# para diametros a la altura del pecho
def boxplot_diametros(df):
  """Mostrar boxplot de diametros.

  Parametros:
    `df` (DataFrame): dataframe.

  Última actualización: 05-10-2021 12:00
  """
  df.boxplot('diametro_altura_pecho', by='ambiente')
# para las alturas
def boxplot_alturas(df):
  """Mostrar boxplot de alturas.

  Parametros:
    `df` (DataFrame): dataframe.

  Última actualización: 05-10-2021 12:00
  """
  df.boxplot('altura_arbol', by='ambiente')

#%%
def main():
  """Main. Ejecutar todas las funciones."""
  directorio = '../Data'
  archivo_arbolado_verdes = 'arbolado-en-espacios-verdes.csv'
  archivo_arbolado_lineal = 'arbolado-publico-lineal-2017-2018.csv'

  fname_arbolado_verdes = os.path.join(directorio, archivo_arbolado_verdes)
  fname_arbolado_lineal = os.path.join(directorio, archivo_arbolado_lineal)

  df_parques = parques(fname_arbolado_verdes)
  df_veredas = veredas(fname_arbolado_lineal)

  df_tipas_parques = tipas_parques(df_parques)
  df_tipas_veredas = tipas_veredas(df_veredas)

  df_tipas = juntar_datasets(df_tipas_parques, df_tipas_veredas)
  
  boxplot_diametros(df_tipas)
  boxplot_alturas(df_tipas)

#%%
if __name__ == '__main__':
  main()
