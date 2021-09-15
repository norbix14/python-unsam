#!/usr/bin/env python3
# fileparse.py

import csv

######################################################################

# 6.3 - Funciones

#%% 6.6, 6.7, 6.8, 6.9
def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
  """Parsear un archivo csv en una lista de registros.
  Se puede seleccionar sólo un subconjunto de las columnas
  determinado por el parámetro `select`, que debe ser una lista de
  nombres de las columnas a considerar.

  Parametros:
    `nombre_archivo` (str): archivo csv.
    `select` (list): especificar que campos mostrar.
    `types` (list): especificar de que tipo deben ser los valores devueltos.
    `has_headers` (bool): especificar si el archivo csv especificado tiene
    cabeceras o no.

  Ejemplo:
    >>> from pprint import pprint
    # se mostraran algunos elementos a modo de ejemplo
    >>> pprint(parse_csv('../Data/camion.csv'))
    [{'cajones': '100', 'nombre': 'Lima', 'precio': '32.2'},
     {'cajones': '50', 'nombre': 'Naranja', 'precio': '91.1'},
     {'cajones': '150', 'nombre': 'Caqui', 'precio': '103.44'}]
    >>> pprint(parse_csv('../Data/camion.csv', types=[str, int, float]))
    [{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
     {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
     {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44}]
    >>> pprint(parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int]))
    [{'cajones': 100, 'nombre': 'Lima'},
     {'cajones': 50, 'nombre': 'Naranja'},
     {'cajones': 150, 'nombre': 'Caqui'}]
    >>> pprint(parse_csv('../Data/precios.csv', types=[str, float], has_headers=False))
    [('Lima', 40.22),
     ('Uva', 24.85),
     ('Ciruela', 44.85)]
  """
  errores = []
  registros = []
  indices = None
  with open(nombre_archivo) as f:
    rows = csv.reader(f)
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
      except:
        errores.append({'line': i, 'msg': 'error en linea'})
  return registros
