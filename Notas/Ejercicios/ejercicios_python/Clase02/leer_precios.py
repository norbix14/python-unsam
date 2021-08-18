#!/usr/bin/env python3
# leer_precios.py

import csv
from pprint import pprint

######################################################################
"""
@author: Norberto Fabrizio
"""

# 2.17

#%% definicion de la funcion
def leer_precios(nombre_archivo):
  """Mostrar el precio de venta de los cajones en el negocio.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.

  Ejemplo:
    >>> from pprint import pprint
    >>> precios = leer_precios('../Data/precios.csv')
    >>> pprint(precios)
    # se muestran algunos elementos a modo de ejemplo
    {'Acelga': 29.26,
     'Ajo': 15.19,
     'Batata': 55.16,
     'Berenjena': 28.47,
     'Bruselas': 15.72,
     'Caqui': 105.46,
     'Cebolla': 58.99,
     'Cebollín': 57.1,
     'Cereza': 11.27,
     'Ciruela': 44.85}
  """
  diccionario = {}
  errores = 0
  try:
    with open(nombre_archivo, 'rt') as archivo:
      filas = csv.reader(archivo)
      for fila in filas:
        try:
          nombre = fila[0]
          precio = float(fila[1])
          diccionario[nombre] = precio
        except IndexError:
          errores += 1
    return diccionario
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#%% precios de los cajones
precios = leer_precios('../Data/precios.csv')

#%% ver precios
pprint(precios)
