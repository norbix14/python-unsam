#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# fileparse.py

import csv

###############################################################################

# 6.3, 7.2 - Funciones, Control de errores

#%% 6.6 - 6.7 - 6.8 - 6.9 - 7.1 - 7.2 - 7.3 - 7.6
def parse_csv(
  nombre_archivo,
  select = None,
  types = None,
  has_headers = True,
  silence_errors = False):
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
    >>> from pprint import pprint

    >>> nombre_archivo = open('../Data/camion.csv', 'rt', encoding='UTF-8')
    # se mostraran algunos elementos a modo de ejemplo

    >>> pprint(parse_csv(nombre_archivo))
    [{'cajones': '100', 'nombre': 'Lima', 'precio': '32.2'},
     {'cajones': '50', 'nombre': 'Naranja', 'precio': '91.1'}]

    >>> pprint(parse_csv(nombre_archivo, types=[str, int, float]))
    [{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
     {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1}]

    >>> pprint(parse_csv(nombre_archivo, select=['nombre', 'cajones'], types=[str, int]))
    [{'cajones': 100, 'nombre': 'Lima'},
     {'cajones': 50, 'nombre': 'Naranja'}]

  Ultima actualizacion: 22-09-21 09:30
  """
  if (select and not has_headers):
    raise RuntimeError('Para seleccionar campos, necesito encabezados.')
  registros = []
  indices = None
  rows = csv.reader(nombre_archivo)
  if has_headers:
    headers = next(rows)
    if select:
      indices = [
        headers.index(nombre_columna)
        for nombre_columna in select
      ]
      headers = select
    else:
      indices = []
  for i, row in enumerate(rows):
    try:
      if not row:
        continue
      if indices:
        row = [row[i] for i in indices]
      if types:
        row = [func(val) for func, val in zip(types, row)]
      registro = dict(zip(headers, row)) if has_headers else tuple(row)
      registros.append(registro)
    except ValueError as e:
      if not silence_errors:
        print(f'Fila {i}: No pude convertir {row}')
        print(f'Fila {i}: Motivo: {e}')
  return registros
