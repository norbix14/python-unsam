#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# informe_final.py
"""
@author: Norberto Fabrizio
"""

import sys

from fileparse import parse_csv

# 6.2 - Scripting

#%% 6.4 - estructurar programa

#%% Clase03_3.13, Clase07_7.7 - 
def leer_camion(nombre_archivo):
  """Mostrar el precio de costo de los cajones en el camion.

  Parametros:
    `nombre_archivo` (any): iterable a recorrer.

  Ejemplo:
    >>> nombre_archivo = open('../Data/camion.csv', 'rt', encoding='UTF-8')
    >>> leer_camion(nombre_archivo)[:1]
    [{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}]

  Ultima actualizacion: 22-09-21 09:30
  """
  return parse_csv(nombre_archivo, types=[str, int, float])

#%% Clase03_3.13, Clase07_7.7 - 
def leer_precios(nombre_archivo):
  """Mostrar el precio de venta de los cajones en el negocio.

  Parametros:
    `nombre_archivo` (any): iterable a recorrer.

  Ejemplo:
    >>> nombre_archivo = open('../Data/precios.csv', 'rt', encoding='UTF-8')
    >>> leer_precios(nombre_archivo)[:1]
    [('Acelga', 29.26)]

  Ultima actualizacion: 22-09-21 09:30
  """
  return parse_csv(nombre_archivo, types=[str, float], has_headers=False)

#%% Clase03_3.13 - 
def hacer_informe(camion = [], precios = []):
  """Generar un informe.

  Parametros:
    `camion` (list): carga de un camion con el precio de costo.
    `precios` (list): precio de venta de la carga del camion.

  Ejemplo:
    >>> camion_csv = open('../Data/camion.csv', 'rt', encoding='UTF-8')
    >>> precios_csv = open('../Data/precios.csv', 'rt', encoding='UTF-8')

    >>> camion = leer_camion(camion_csv)
    >>> precios = leer_precios(precios_csv)

    >>> hacer_informe(camion, precios)[:1]
    [('Lima', 100, 32.2, 8.019999999999996)]

  Ultima actualizacion: 27-09-21 09:30
  """
  inventario = []
  for producto in camion:
    try:
      cambio = 0.0
      nombre = producto['nombre']
      cajones = producto['cajones']
      precio = producto['precio']
      for producto, precio_venta in precios:
        if (producto == nombre):
          cambio = precio_venta - precio
      tupla = (nombre, cajones, precio, cambio)
      inventario.append(tupla)
    except:
      pass
  return inventario

#%% 6.4 - 
def imprimir_informe(informe = []):
  """Imprimir por pantalla una tabla con datos del informe.

  Parametros:
    `informe` (list): listado de tuplas con el balance entre el
    costo y la ganancia.

  Ejemplo:
    >>> camion_csv = open('../Data/camion.csv', 'rt', encoding='UTF-8')
    >>> precios_csv = open('../Data/precios.csv', 'rt', encoding='UTF-8')

    >>> camion = leer_camion(camion_csv)
    >>> precios = leer_precios(precios_csv)

    >>> informe = hacer_informe(camion, precios)
    >>> imprimir_informe(informe)
    # se muestra una tabla formateada por pantalla

  Ultima actualizacion: 17-09-21 16:16
  """
  cabeceras = ('Nombre', 'Cajones', 'Precio', 'Cambio')
  encabezado = f'%10s %10s %10s %10s' % cabeceras
  separador = ('-' * 10 + ' ') * len(cabeceras)
  print(encabezado)
  print(separador)
  for dato in informe:
    print('%10s %10d %10.2f %10.2f' % dato)
  print()

#%% 6.5 - 
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
  """Realizar el informe y luego mostrarlo por pantalla.

  Parametros:
    `nombre_archivo_camion` (any): iterable a recorrer.
    `nombre_archivo_precios` (any): iterable a recorrer.

  Ejemplo:
    >>> camion = open('../Data/camion.csv', 'rt', encoding='UTF-8')
    >>> precios = open('../Data/precios.csv', 'rt', encoding='UTF-8')

    >>> informe_camion(camion, precios)
    # realiza el informe y luego muestra una tabla formateada por pantalla

  Ultima actualizacion: 22-09-21 09:30
  """
  camion = leer_camion(nombre_archivo_camion)
  precios = leer_precios(nombre_archivo_precios)
  datos_informe = hacer_informe(camion, precios)
  imprimir_informe(datos_informe)

#%% 7.4 - funcion principal
def f_principal(parametros = []):
  """Funcion principal.

  Parametros:
    `parametros` (list): listado de parametros pasados por linea
    de comandos.

  Ultima actualizacion: 21-09-21 15:30
  """
  args = len(parametros)
  file = parametros[0] if args > 0 else 'informe_final.py'
  if (args <= 1):
    print('-- Modo de uso --')
    print(f'{file} [camion_csv] [precios_csv]')
    print('')
    print('Parametro [camion_csv]: archivo con los datos de los productos.')
    print('Parametro [precios_csv]: archivo con los datos de los precios.')
    print('')
    print(f'EJEMPLO: {file} ../Data/camion.csv ../Data/precios.csv')
  else:
    if (args < 3):
      print('Se requieren dos rutas de dos archivos distintos.')
      print(f'EJEMPLO: {file} ../Data/camion.csv ../Data/precios.csv')
    else:
      camion = open(parametros[1], 'rt', encoding='UTF-8')
      precios = open(parametros[2], 'rt', encoding='UTF-8')
      informe_camion(camion, precios)
      camion.close()
      precios.close()

#%% main
if __name__ == '__main__':
  f_principal(sys.argv)
