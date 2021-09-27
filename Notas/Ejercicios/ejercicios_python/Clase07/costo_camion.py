#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# costo_camion.py
"""
@author: Norberto Fabrizio
"""

import sys

import informe_final

# 3.9

#%% Clase03_3.9 - 
def costo_camion(nombre_archivo):
  """Calcular el costo total pagado por los cajones.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.

  Ejemplo:
    >>> costo_camion('../Data/camion.csv')
    47671.15

  Ultima actualizacion: 27-09-21 16:30
  """
  try:
    with open(nombre_archivo, 'rt', encoding='UTF-8') as archivo:
      camion = informe_final.leer_camion(archivo)
      return float(sum([
        producto['cajones'] * producto['precio']
        for producto in camion
      ]))
  except FileNotFoundError:
    print(f'No existe el archivo o carpeta "{nombre_archivo}".')
    return 0.0

#%% 7.4 - funcion principal
def f_principal(parametros):
  """Funcion principal.

  Parametros:
    `parametros` (list): listado de parametros pasados por linea
    de comandos.

  Ultima actualizacion: 21-09-21 09:00
  """
  if (len(parametros) <= 1):
    print('-- Modo de uso --')
    print(f'{parametros[0]} [csv]')
    print('Parametro [csv]: archivo con los datos')
    print(f'EJEMPLO: {parametros[0]} ../Data/camion.csv')
  else:
    print(costo_camion(parametros[1]))

#%% main
if __name__ == '__main__':
  f_principal(sys.argv)
