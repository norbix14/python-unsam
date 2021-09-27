#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# leer_precios.py
"""
@author: Norberto Fabrizio
"""

import csv

# 2.17

#%% definicion de la funcion
def leer_precios(nombre_archivo):
  """Mostrar el precio de venta de los cajones en el negocio.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.

  Ejemplo:
    >>> leer_precios('../Data/precios.csv')
    # se muestran algunos elementos a modo de ejemplo
    {'Acelga': 29.26, 'Ajo': 15.19}
  """
  try:
    diccionario = {}
    errores = 0
    with open(nombre_archivo, 'rt', encoding='UTF-8') as archivo:
      filas = csv.reader(archivo)
      for fila in filas:
        try:
          nombre = fila[0]
          precio = float(fila[1])
          diccionario[nombre] = precio
        except:
          errores += 1
    return diccionario
  except FileNotFoundError:
    print(f'No existe el archivo o carpeta "{nombre_archivo}".')
    return {}

#%%
if __name__ == '__main__':
  precios = leer_precios('../Data/precios.csv')
  print(precios)
