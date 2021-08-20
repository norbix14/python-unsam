#!/usr/bin/env python3
# tabla_informe.py

import csv

######################################################################
"""
@author: Norberto Fabrizio
"""

# 3.13

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
      for i, fila in enumerate(filas, start = 0):
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

#%% funcion hacer_informe(camion, precios)
def hacer_informe(camion, precios):
  """Generar un informe.

  Parametros:
    `camion` (list): lista de diccionarios con datos de la carga
    de un camion.
    `precios` (dict): diccionario con datos como el producto y su 
    precio.

  Ejemplo:
    >>> from pprint import pprint
    >>> camion = leer_camion('../Data/camion.csv')
    >>> precios = leer_precios('../Data/precios.csv')
    >>> informe = hacer_informe(camion, precios)
    >>> pprint(informe)
    [('Lima', 100, 32.2, 8.019999999999996),
     ('Naranja', 50, 91.1, 15.180000000000007),
     ('Caqui', 150, 103.44, 2.019999999999996),
     ('Mandarina', 200, 51.23, 29.660000000000004),
     ('Durazno', 95, 40.37, 33.11000000000001),
     ('Mandarina', 50, 65.1, 15.790000000000006),
     ('Naranja', 100, 70.44, 35.84)]
  """
  inventario = []
  for producto in camion:
    cambio = 0.0
    nombre = producto['nombre']
    cajones = int(producto['cajones'])
    precio = float(producto['precio'])
    cambio = precios[nombre] - precio
    tupla = (nombre, cajones, precio, cambio)
    inventario.append(tupla)
  return inventario

#%% funcion tabla_con_formato(informe)
def tabla_con_formato(informe = []):
  """Toma una lista y muestra una salida bien formateada.

  Parametros:
    `informe` (list): lista a iterar.
  """
  sep = '-'
  col1, col2, col3, col4 = ('Nombre', 'Cajones', 'Precio', 'Cambio')
  encabezado = f'{col1:>10s} {col2:>10s} {col3:>10s} {col4:>10s}'
  separador = f'{sep:->10s} {sep:->10s} {sep:->10s} {sep:->10s}'
  print(encabezado)
  print(separador)
  for r in informe:
    print('%10s %10d %10.2f %10.2f' % r)

#%% archivos csv
nombre_archivo_camion = '../Data/camion.csv'
nombre_archivo_precios = '../Data/precios.csv'

#%% leer archivos
camion = leer_camion(nombre_archivo_camion)
precios = leer_precios(nombre_archivo_precios)

#%% hacer el informe
informe = hacer_informe(camion, precios)

#%% mostrar tabla bien formateada con el informe
tabla_con_formato(informe)
