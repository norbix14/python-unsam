#!/usr/bin/env python3
# informe.py

import csv

######################################################################
"""
@author: Norberto Fabrizio
"""

# 2.18

#%% funcion leer_camion(nombre_archivo)
def leer_camion(nombre_archivo):
  """Mostrar el precio de costo de los cajones en el camion.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.

  Ejemplo:
    >>> from pprint import pprint
    >>> camion = leer_camion('../Data/camion.csv')
    >>> pprint(camion)
    # se muestran algunos elementos a modo de ejemplo
    [{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2},
     {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1},
     {'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44},
     {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23},
     {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}]
  """
  camion = []
  errores = 0
  try:
    with open(nombre_archivo, 'rt') as archivo:
      filas = csv.reader(archivo)
      next(filas) # headers
      for fila in filas:
        try:
          lote = {
            'nombre': fila[0],
            'cajones': int(fila[1]),
            'precio': float(fila[2])
          }
          camion.append(lote)
        except ValueError:
          errores += 1
    return camion
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#%% funcion leer_precios(nombre_archivo)
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

#%% funcion informe()
def informe():
  """Generar informe y mostrar el costo de camion,
  las ventas en el negocio y un balance final.

  Ejemplo:
    >>> informe()
    'Costo camion: $47671.15'
    'Venta en negocio: $62986.1'
    'Hay una ganancia de $15314.95'
  """
  costo_camion = 0.0
  costo_negocio = 0.0
  balance = ''
  try:
    precio_costo = leer_camion('../Data/camion.csv')
    precio_venta = leer_precios('../Data/precios.csv')
    for producto in precio_costo:
      nombre = producto['nombre']
      cajones = producto['cajones']
      precio = producto['precio']
      costo_camion += cajones * precio
      if (nombre in precio_venta):
        costo_negocio += cajones * precio_venta[nombre]
    if (costo_negocio > costo_camion):
      ganancia = round(costo_negocio - costo_camion, 2)
      balance = f'Hay una ganancia de ${ganancia}'
    else:
      perdida = round(costo_camion - costo_negocio, 2)
      balance = f'Hay una perdida de ${perdida}'
    print(f'Costo camion: ${costo_camion}')
    print(f'Venta en negocio: ${costo_negocio}')
    print(balance)
  except FileNotFoundError:
    print('No existe el archivo o carpeta')

#%% ver informe
informe()
