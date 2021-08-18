#!/usr/bin/env python3
# camion_commandline.py

import csv, sys

######################################################################
"""
@author: Norberto Fabrizio
"""

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

    >>> py camion_commandline.py '../Data/missing.csv'
    30381.15

    >>> py camion_commandline.py '../Data/camioneta.csv'
    'No existe el archivo o carpeta'
  """
  nombre_archivo = '../Data/camion.csv'
  costo_total = 0.0
  args = sys.argv[1:]
  if (len(args) > 0):
    nombre_archivo = args[0]
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

#%% ver costo del camion
print(costo_camion())
