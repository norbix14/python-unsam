#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vigilante.py
"""
@author: Norberto Fabrizio
"""

import os

import time

from informe_final import leer_camion

# 10.3 - Iteracion a medida
# 10.4 - Productores, consumidores y cañerias

#%% 10.5, 10.6, 10.7 - 
def vigilar(filename):
  """Indicador de precios en tiempo real.

  Parametros:
    `filename` (str): ruta al archivo csv.

  Última actualización: 12-10-2021 15:00
  """
  with open(filename, 'rt', encoding='UTF-8') as f:
    f.seek(0, os.SEEK_END)
    while True:
      line = f.readline()
      if line == '':
        time.sleep(0.5)
        continue
      yield line

#%% 10.8 - 
def filematch(lines, substr):
  """Filtrar elementos.

  Parametros:
    `lines` (any): algun elemento iterable.
    `substr` (str): elemento a buscar dentro del iterable.

  Última actualización: 11-10-2021 19:30
  """
  for line in lines:
    if substr in line:
      yield line

#%% 10.7
if __name__ == '__main__':
  directorio = 'Data'
  mercado_csv = 'mercadolog.csv'
  camion_csv = 'camion.csv'

  archivo_camion = os.path.join('..', directorio, camion_csv)
  archivo_mercado = os.path.join('..', directorio, mercado_csv)

  with open(archivo_camion, 'rt', encoding='UTF-8') as f:
    camion = leer_camion(f)
    for line in vigilar(archivo_mercado):
      fields = line.split(',')
      nombre = fields[0].strip('"')
      precio = float(fields[1])
      volumen = int(fields[2])
      if nombre in camion:
        print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
