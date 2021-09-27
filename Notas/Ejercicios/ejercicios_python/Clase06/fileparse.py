#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# fileparse.py
"""
@author: Norberto Fabrizio
"""

import csv

# 6.3 - Funciones

#%% 6.6, 6.7, 6.8, 6.9
def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
  """Parsear un archivo csv en una lista de registros.

  Se puede seleccionar sólo un subconjunto de las columnas
  determinado por el parámetro `select`, que debe ser una lista de
  nombres de las columnas a considerar.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.
    `select` (list): especificar que campos mostrar.
    `types` (list): especificar de que tipo deben ser los valores devueltos.
    `has_headers` (bool): especificar si el archivo csv especificado tiene
    cabeceras o no.

  Ejemplo:
    >>> camion = '../Data/camion.csv'
    >>> precios = '../Data/precios.csv'

    >>> parse_csv(camion)[:1]
    [{'cajones': '100', 'nombre': 'Lima', 'precio': '32.2'}]

    >>> parse_csv(camion, types=[str, int, float])[:1]
    [{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2}]

    >>> parse_csv(camion, select=['nombre', 'cajones'], types=[str, int])[:1]
    [{'cajones': 100, 'nombre': 'Lima'}]

    >>> parse_csv(precios, types=[str, float], has_headers=False)[:1]
    [('Lima', 40.22)]
  """
  try:
    errores = []
    registros = []
    indices = None
    with open(nombre_archivo, 'rt', encoding='UTF-8') as archivo:
      filas = csv.reader(archivo)
      if has_headers:
        cabeceras = next(filas)
        if select:
          indices = [
            cabeceras.index(nombre_columna)
            for nombre_columna in select
          ]
          cabeceras = select
        else:
          indices = []
      for i, fila in enumerate(filas):
        try:
          if not fila:
            continue
          if indices:
            fila = [fila[i] for i in indices]
          if types:
            fila = [func(val) for func, val in zip(types, fila)]
          registro = dict(zip(cabeceras, fila)) if has_headers else tuple(fila)
          registros.append(registro)
        except:
          errores.append({'line': i, 'msg': 'error en linea'})
    return registros
  except FileNotFoundError:
    print(f'No existe el archivo o carpeta "{nombre_archivo}".')
    return []
