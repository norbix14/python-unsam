#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# camion_commandline.py
"""
@author: Norberto Fabrizio
"""

import sys

import csv

# 2.10

#%% definicion de la funcion
def costo_camion():
  """Calcular el costo total pagado por los cajones.

  Observaciones:
    * En Linux, utilizo alias para ejecutar python3.
    * Alias:
    * `py`, ejecutar normalmente (`python3 archivo.py`).
    * `pyi`, ejecutar interactivamente (`python3 -i archivo.py`).

  Ejemplo:
    >>> py camion_commandline.py
    # usa '../Data/camion.csv' por defecto.
    47671.15

    >>> py camion_commandline.py '../Data/camion2.csv'
    19908.75
  """
  try:
    args = sys.argv
    nombre_archivo = '../Data/camion.csv'
    costo_total = 0.0
    if (len(args) > 1):
      nombre_archivo = args[1]
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
  print(costo_camion())
