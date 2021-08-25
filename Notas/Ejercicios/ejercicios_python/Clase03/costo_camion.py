#!/usr/bin/env python3
# costo_camion.py

import csv

######################################################################
"""
@author: Norberto Fabrizio
"""

# 3.8

#%% definicion de la funcion
def costo_camion(nombre_archivo):
  """Calcular el costo total pagado por los cajones.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.

  Ejemplo:
    >>> costo = costo_camion('ruta/al/archivo/csv')
    >>> print(costo)
    123456789.0 # dependiendo del archivo pasado
  """
  costo_total = 0.0
  try:
    with open(nombre_archivo, 'rt') as archivo:
      filas = csv.reader(archivo)
      encabezados = next(filas)
      for n_fila, fila in enumerate(filas, start = 0):
        record = dict(zip(encabezados, fila))
        try:
          cajones = int(record['cajones'])
          precio = float(record['precio'])
          costo_total += cajones * precio
        except ValueError:
          print(f'Fila {n_fila}: No puede interpretar {fila}')
    return costo_total
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#%% 
if __name__ == '__main__':
  #%% archivo csv
  nombre_archivo = '../Data/camion.csv'

  #%% calcular costo
  costo = costo_camion(nombre_archivo)

  #%% ver costo
  print(costo)
