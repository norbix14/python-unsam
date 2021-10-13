#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# formato_tabla.py
"""
@author: Norberto Fabrizio
"""

# 9.3 - Herencia
# 9.4 - Metodos especiales

#%% 9.5 - un problema de extensibilidad
class FormatoTabla():
  """Clase base para crear una tabla formateada."""
  def encabezado(self, headers):
    """Crear el encabezado de la tabla.

    Parametros:
      `headers` (list): listado de encabezados.
    """
    raise NotImplementedError()

  def fila(self, rowdata):
    """Crear una unica fila de datos de la tabla.

    Parametros:
      `rowdata` (list): listado de elementos.
    """
    raise NotImplementedError()

#%% 9.6 - usemos herencia para cambiar la salida
# formato txt
class FormatoTablaTXT(FormatoTabla):
  """Clase para generar una tabla en formato TXT."""
  def encabezado(self, headers):
    """Crear el encabezado de la tabla con distancias iguales.

    Parametros:
      `headers` (list): listado de encabezados.
    """
    for h in headers:
      print(f'{h:>10s}', end=' ')
    print()
    print(('-' * 10 + ' ') * len(headers))

  def fila(self, rowdata):
    """Crear una unica fila de datos de la tabla separada por espacios
    iguales.

    Parametros:
      `rowdata` (list): listado de elementos.
    """
    for d in rowdata:
      print(f'{d:>10s}', end=' ')
    print()
# formato csv
class FormatoTablaCSV(FormatoTabla):
  """Clase para generar una tabla en formato CSV."""
  def encabezado(self, headers):
    """Crear el encabezado de la tabla separado por comas.

    Parametros:
      `headers` (list): listado de encabezados.
    """
    print(','.join(headers))

  def fila(self, rowdata):
    """Crear una unica fila de datos de la tabla separada por comas.

    Parametros:
      `rowdata` (list): listado de elementos.
    """
    print(','.join(rowdata))
# formato html
class FormatoTablaHTML(FormatoTabla):
  """Clase para generar una tabla en formato HTML."""
  def encabezado(self, headers):
    """Crear el encabezado de la tabla mediante etiquetas HTML de una tabla.

    Parametros:
      `headers` (list): listado de encabezados.
    """
    rows = ''
    for h in headers:
      rows += f'<th>{h}</th>'
    print(f'<tr>{rows}</tr>')

  def fila(self, rowdata):
    """Crear una unica fila de datos de la tabla mediante etiquetas HTML
    de una tabla.

    Parametros:
      `rowdata` (list): listado de elementos.
    """
    rows = ''
    for d in rowdata:
      rows += f'<td>{d}</td>'
    print(f'<tr>{rows}</tr>')

#%% 9.7 - polimorfismo en accion
def crear_formateador(extension):
  """Crear el formateador adecuado segun la extension elegida.

  Parametros:
    `extension` (str): tipo de salida que tendran los datos. puede ser
    `txt`, `csv` o `html`.
  """
  if (extension == 'csv'):
    return FormatoTablaCSV()
  elif (extension == 'html'):
    return FormatoTablaHTML()
  elif (extension == 'txt'):
    return FormatoTablaTXT()
  else:
    raise RuntimeError(f'Formato "{extension}" no reconocido.')

#%% 9.10 - ejemplo de getattr()
def imprimir_tabla(datos, atributos, formateador):
  """Mostrar una tabla a partir de un listado de atributos especificados
  por el usuario.

  Parametros:
    `datos` (list): listado de datos con los que trabajar.
    `atributos` (list): listado de atributos.
    `formateador` (any): formateador para elegir el tipo de salida.

  última actualización: 08-10-2021 11:30
  """
  formateador.encabezado(atributos)
  for data in datos:
    rowdata = [str(getattr(data, attr)) for attr in atributos]
    formateador.fila(rowdata)
