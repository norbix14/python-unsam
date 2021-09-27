#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tabla_informe.py
"""
@author: Norberto Fabrizio
"""

import csv

# 3.13

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

#%% funcion hacer_informe(camion, precios)
def hacer_informe(camion = [], precios = {}):
  """Generar un informe.

  Parametros:
    `camion` (list): carga de un camion con el precio de costo.
    `precios` (dict): precio de venta de la carga del camion.

  Ejemplo:
    >>> camion = leer_camion('../Data/camion.csv')
    >>> precios = leer_precios('../Data/precios.csv')
    >>> hacer_informe(camion, precios)[:1]
    [('Lima', 100, 32.2, 8.019999999999996)]
  """
  inventario = []
  for producto in camion:
    try:
      cambio = 0.0
      nombre = producto['nombre']
      cajones = producto['cajones']
      precio = producto['precio']
      cambio = precios[nombre] - precio
      tupla = (nombre, cajones, precio, cambio)
      inventario.append(tupla)
    except:
      pass
  return inventario

#%% funcion tabla_con_formato(informe)
def tabla_con_formato(informe = []):
  """Tomar una lista y mostrar una tabla bien formateada por pantalla.

  Parametros:
    `informe` (list): lista a iterar.
  """
  cabeceras = ('Nombre', 'Cajones', 'Precio', 'Cambio')
  encabezado = f'%10s %10s %10s %10s' % cabeceras
  separador = ('-' * 10 + ' ') * len(cabeceras)
  print(encabezado)
  print(separador)
  for dato in informe:
    print('%10s %10d %10.2f %10.2f' % dato)
  print()

#%%
def tests():
  camiones = [
    'camion', 'camion2', 'camion_blancos',
    'fecha_camion', 'missing', 'noexiste'
  ]
  precios = leer_precios('../Data/precios.csv')
  for camion in camiones:
    ruta = f'../Data/{camion}.csv'
    c = leer_camion(ruta)
    informe = hacer_informe(c, precios)
    print(f'{ruta:-^43s}')
    tabla_con_formato(informe)

#%%
def main():
  tests()

#%% 
if __name__ == '__main__':
  main()
