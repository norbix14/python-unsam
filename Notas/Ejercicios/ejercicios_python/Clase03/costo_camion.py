#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# costo_camion.py
"""
@author: Norberto Fabrizio
"""

import csv

# 3.8

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

#%%
def main():
  nombre_archivo = '../Data/camion.csv'
  costo = costo_camion(nombre_archivo)
  print(costo)

#%% 
if __name__ == '__main__':
  main()
