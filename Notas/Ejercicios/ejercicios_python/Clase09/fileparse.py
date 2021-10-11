#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# fileparse.py
"""
@author: Norberto Fabrizio
"""

import csv

# 6.3, 7.2 - Funciones, Control de errores

#%% 6.6 - 6.7 - 6.8 - 6.9 - 7.1 - 7.2 - 7.3 - 7.6
def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = False):
  """Parsear un archivo csv en una lista de registros.

  Se puede seleccionar sólo un subconjunto de las columnas
  determinado por el parámetro `select`, que debe ser una lista de
  nombres de las columnas a considerar.

  Parametros:
    `nombre_archivo` (any): iterable a recorrer.
    `select` (list): especificar que campos mostrar.
    `types` (list): especificar de que tipo deben ser los valores
    devueltos.
    `has_headers` (bool): especificar si el archivo csv especificado
    tiene cabeceras o no.
    `silence_errors` (bool): especificar si se quieren ver o silenciar
    los errores producidos al parsear el archivo csv.

  Ejemplo:
    >>> camion = open('../Data/camion.csv', 'rt', encoding='UTF-8')
    >>> precios = open('../Data/precios.csv', 'rt', encoding='UTF-8')

    >>> parse_csv(camion)[:1]
    [{'cajones': '100', 'nombre': 'Lima', 'precio': '32.2'}]

    >>> parse_csv(camion, types=[str, int, float])[:1]
    [{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2}]

    >>> parse_csv(camion, select=['nombre', 'cajones'], types=[str, int])[:1]
    [{'cajones': 100, 'nombre': 'Lima'}]

    >>> parse_csv(precios, types=[str, float], has_headers=False)[:1]
    [('Acelga', 29.26)]

  Ultima actualizacion: 22-09-21 09:30
  """
  if (select and not has_headers):
    raise RuntimeError('Para seleccionar campos, necesito encabezados.')
  registros = []
  indices = None
  filas = csv.reader(nombre_archivo)
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
    except ValueError as e:
      if not silence_errors:
        print(f'Fila {i}. No pude convertir {fila}')
        print(f'Fila {i}. Motivo: {e}')
  return registros
