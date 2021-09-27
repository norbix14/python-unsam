#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# informe.py
"""
@author: Norberto Fabrizio
"""

import csv

# 2.18
#%% funcion costo_camion - 
def costo_camion(nombre_archivo):
  """Calcular el costo total pagado por los cajones.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.

  Ejemplo:
    >>> costo_camion('../Data/camion.csv')
    47671.15
  """
  try:
    costo_total = 0.0
    with open(nombre_archivo, 'rt', encoding='UTF-8') as archivo:
      filas = csv.reader(archivo)
      next(filas)
      for fila in filas:
        try:
          cajones = int(fila[1])
          precio = float(fila[2])
          costo_total += cajones * precio
        except ValueError as e:
          print(f'Error: {e}')
    return costo_total
  except FileNotFoundError:
    print(f'No existe el archivo o carpeta "{nombre_archivo}".')
    return 0.0

#%% funcion leer_camion - 
def leer_camion(nombre_archivo):
  """Mostrar el precio de costo de los cajones en el camion.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.

  Ejemplo:
    >>> leer_camion('../Data/camion.csv')[:1]
    [{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}]
  """
  try:
    camion = []
    errores = 0
    with open(nombre_archivo, 'rt', encoding='UTF-8') as archivo:
      filas = csv.reader(archivo)
      next(filas)
      for fila in filas:
        try:
          lote = {
            'nombre': fila[0],
            'cajones': int(fila[1]),
            'precio': float(fila[2])
          }
          camion.append(lote)
        except:
          errores += 1
    return camion
  except FileNotFoundError:
    print(f'No existe el archivo o carpeta "{nombre_archivo}".')
    return []

#%% funcion leer_precios - 
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

#%% funcion informe - 
def informe(camion_csv = '../Data/camion.csv', precios_csv = '../Data/precios.csv'):
  """Generar informe y mostrar el costo de camion, las ventas en el negocio
  y un balance final.

  Parametros:
    `camion_csv` (str): ruta al archivo csv.
    `precios_csv` (str): ruta al archivo csv.

  Ejemplo:
    >>> informe('../Data/camion.csv', '../Data/precios.csv')
    'Costo camion: $47671.15'
    'Venta en negocio: $62986.1'
    'Hay una ganancia de $15314.95'
  """
  costo_camion = 0.0
  costo_negocio = 0.0
  balance = ''

  precio_costo = leer_camion(camion_csv)
  precio_venta = leer_precios(precios_csv)

  for producto in precio_costo:
    try:
      nombre = producto['nombre']
      cajones = producto['cajones']
      precio = producto['precio']
      costo_camion += cajones * precio
      if (nombre in precio_venta):
        costo_negocio += cajones * precio_venta[nombre]
    except:
      pass

  if (costo_negocio > costo_camion):
    ganancia = round(costo_negocio - costo_camion, 2)
    balance = f'Hay una ganancia de ${ganancia}'
  else:
    perdida = round(costo_camion - costo_negocio, 2)
    balance = f'Hay una perdida de ${perdida}'

  print(f'Costo camion: ${costo_camion}')
  print(f'Venta en negocio: ${costo_negocio}')
  print(balance)

#%%
def tests():
  camiones = [
    'camion', 'camion2', 'camion_blancos',
    'fecha_camion', 'missing'
  ]
  precios = '../Data/precios.csv'
  for camion in camiones:
    ruta = f'../Data/{camion}.csv'
    print(f'-- Archivo {ruta} --')
    informe(ruta, precios)
    print()

#%%
if __name__ == '__main__':
  tests()
