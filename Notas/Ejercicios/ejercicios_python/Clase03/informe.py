#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# informe.py
"""
@author: Norberto Fabrizio
"""

import csv

# 3.9

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
      encabezados = next(filas)
      for n_fila, fila in enumerate(filas):
        record = dict(zip(encabezados, fila))
        try:
          cajones = int(record['cajones'])
          precio = float(record['precio'])
          costo_total += cajones * precio
        except ValueError:
          print(f'Fila {n_fila}: No puede interpretar {fila}')
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
    with open(nombre_archivo, 'rt', encoding='UTF-8') as archivo:
      filas = csv.reader(archivo)
      encabezados = next(filas)
      for fila in filas:
        try:
          lote = dict(zip(encabezados, fila))
          lote['cajones'] = int(lote['cajones'])
          lote['precio'] = float(lote['precio'])
          camion.append(lote)
        except:
          pass
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
      cabeceras = ['nombre', 'precio']
      for fila in filas:
        producto = dict(zip(cabeceras, fila))
        try:
          nombre = producto['nombre']
          precio = float(producto['precio'])
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

  carga_camion = leer_camion(camion_csv)
  listado_precios = leer_precios(precios_csv)

  for producto in carga_camion:
    try:
      nombre = producto['nombre']
      cajones = producto['cajones']
      precio = producto['precio']
      costo_camion += cajones * precio
      costo_negocio += cajones * listado_precios[nombre]
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
  print()

#%%
def tests():
  camiones = [
    'camion', 'camion2', 'camion_blancos',
    'fecha_camion', 'missing', 'noexiste'
  ]
  precios = '../Data/precios.csv'
  for camion in camiones:
    ruta = f'../Data/{camion}.csv'
    print(f'{ruta:-^43s}')
    informe(ruta, precios)

#%%
def main():
  tests()

#%% 
if __name__ == '__main__':
  main()
