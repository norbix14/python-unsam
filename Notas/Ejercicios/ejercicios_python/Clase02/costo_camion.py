#!/usr/bin/env python3
# costo_camion.py

import csv

######################################################################
"""
@author: Norberto Fabrizio
"""

# 2.6

#%% definicion de la funcion
def costo_camion(nombre_archivo):
  """Calcular el costo total pagado por los cajones.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.

  Ejemplo:
    >>> costo = costo_camion('../Data/camion.csv')
    >>> print(costo)
    47671.15
  """
  costo_total = 0.0
  try:
    with open(nombre_archivo, 'rt') as archivo:
      filas = csv.reader(archivo)
      next(filas) # headers
      for fila in filas:
        try:
          cajones = int(fila[1])
          precio = float(fila[2])
          costo_total += cajones * precio
        except ValueError as e:
          print(f'Error: {e}')
    return costo_total
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#%% calcular costo
costo = costo_camion('../Data/camion.csv')

#%% ver costo del camion
print(f'Costo total: ${costo}')
