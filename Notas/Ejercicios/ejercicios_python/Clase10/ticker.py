#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ticker.py
"""
@author: Norberto Fabrizio
"""

import csv

from formato_tabla import crear_formateador

from informe_final import leer_camion

from vigilante import vigilar

# 10.4 - Productores, consumidores y cañerias

#%% 10.10, 10.15 - 
#
def cambiar_tipo(rows, types):
  """Elegir los tipos de los datos a devolver.

  Parámetros:
    `rows` (any): algún elemento iterable.
    `types` (list): listado con los tipos.

  Última actualización: 12-10-2021 17:00
  """
  return ([func(val) for func, val in zip(types, row)] for row in rows)
#
def hacer_dicts(rows, headers):
  """Crear un diccionario con los datos especificados.

  Parámetros:
    `rows` (any): algún elemento iterable.
    `headers` (list): listado con las cabeceras del elemento iterable.

  Última actualización: 12-10-2021 17:00
  """
  return (dict(zip(headers, row)) for row in rows)
#
def elegir_columnas(rows, indexes):
  """Elegir que columnas mostrar del elemento iterable.

  Parámetros:
    `rows` (any): algún elemento iterable.
    `indexes` (list): indices elegidos.

  Última actualización: 12-10-2021 17:00
  """
  return ([row[index] for index in indexes] for row in rows)
#
def filtrar_datos(rows, names):
  """Filtrar los datos a devolver según el criterio especificado en `names`.

  Parámetros:
    `rows` (any): algún elemento iterable.
    `names` (list): listado con datos contra el cual comparar.

  Última actualización: 12-10-2021 17:00
  """
  return (row for row in rows if row['nombre'] in names)
#
def parsear_datos(lines):
  """Parsear los datos mediante `csv reader`, elegir que columnas mostrar,
  elegir el tipo del dato a devolver y retornar un elemento iterable.

  Parámetros:
    `lines` (any): algún elemento iterable.

  Última actualización: 12-10-2021 22:00
  """
  rows = csv.reader(lines)
  rows = elegir_columnas(rows, [0, 1, 2])
  rows = cambiar_tipo(rows, [str, float, int])
  return hacer_dicts(rows, ['nombre', 'precio', 'volumen'])

#%% 10.12
def ticker(camion_file, log_file, formato):
  """Crear un indicador en tiempo real.

  Parámetros:
    `camion_file` (str): archivo csv con los datos del camion.
    `log_file` (str): archivo csv en donde mirar los datos.
    `formato` (str): formato de salida de los datos por pantalla.

  Ejemplo:
    >>> ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')
    # muestra una tabla formateada segun el formato elegido

  Última actualización: 12-10-2021 22:00
  """
  try:
    with open(camion_file, 'rt', encoding='UTF-8') as f:
      formateador = crear_formateador(formato)
      rows = parsear_datos(vigilar(log_file))
      rows = filtrar_datos(rows, leer_camion(f))
      formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
      for row in rows:
        formateador.fila([
          f"{row['nombre']}",
          f"{row['precio']:0.2f}",
          f"{row['volumen']}"
        ])
  except FileNotFoundError as e:
    print(f'Error: {e}')
