#!/usr/bin/env python3
# informe.py

import csv
from collections import Counter

######################################################################
"""
@author: Norberto Fabrizio
"""

# 3.9

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
  try:
    camion = []
    with open(nombre_archivo, 'rt') as archivo:
      filas = csv.reader(archivo)
      encabezados = next(filas)
      for n_fila, fila in enumerate(filas, start = 0):
        lote = dict(zip(encabezados, fila))
        camion.append(lote)
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
  try:
    diccionario = {}
    errores = 0
    with open(nombre_archivo, 'rt') as archivo:
      filas = csv.reader(archivo)
      cabeceras = ['nombre', 'precio']
      for fila in filas:
        producto = dict(zip(cabeceras, fila))
        try:
          nombre = producto['nombre']
          precio = float(producto['precio'])
          diccionario[nombre] = precio
        except ValueError:
          errores += 1
        except IndexError:
          errores += 1
        except KeyError:
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
  try:
    costo_camion = 0.0
    costo_negocio = 0.0
    balance = ''
    # 3.11
    #tenencias_camion_uno = Counter()
    #tenencias_camion_dos = Counter()
    carga_camion = leer_camion('../Data/camion.csv')
    listado_precios = leer_precios('../Data/precios.csv')
    # 3.11
    #carga_camion_dos = leer_camion('../Data/camion2.csv')

    for producto in carga_camion:
      nombre = producto['nombre']
      cajones = int(producto['cajones'])
      precio = float(producto['precio'])
      costo_camion += cajones * precio
      costo_negocio += cajones * listado_precios[nombre]
      # 3.11
      #tenencias_camion_uno[nombre] += cajones

    # 3.11
    """
    for producto in carga_camion_dos:
      nombre = producto['nombre']
      cajones = int(producto['cajones'])
      tenencias_camion_dos[nombre] += cajones
    tenencias_totales = tenencias_camion_uno + tenencias_camion_dos
    """

    if (costo_negocio > costo_camion):
      ganancia = round(costo_negocio - costo_camion, 2)
      balance = f'Hay una ganancia de ${ganancia}'
    else:
      perdida = round(costo_camion - costo_negocio, 2)
      balance = f'Hay una perdida de ${perdida}'

    print(f'Costo camion: ${costo_camion}')
    print(f'Venta en negocio: ${costo_negocio}')
    print(balance)
    # 3.11
    #print('\nTenencias totales:')
    #print(tenencias_totales)
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#%% 
if __name__ == '__main__':
  informe()
