#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# costo_camion.py
"""
@author: Norberto Fabrizio
"""

import csv

# 2.6

#%% definicion de la funcion
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

#%%
if __name__ == '__main__':
  costo = costo_camion('../Data/camion.csv')
  print(f'Costo total: ${costo}')
