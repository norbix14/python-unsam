#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# informe_funciones.py
"""
@author: Norberto Fabrizio
"""

from fileparse import parse_csv

# 6.2 - Scripting

#%% 6.4 - estructurar programa

#%% Clase03_3.13 - 
def leer_camion(nombre_archivo = '../Data/camion.csv'):
  """Mostrar el precio de costo de los cajones en el camion.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.

  Ejemplo:
    >>> leer_camion('../Data/camion.csv')[:1]
    [{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}]
  """
  return parse_csv(nombre_archivo, types=[str, int, float])

#%% Clase03_3.13 - 
def leer_precios(nombre_archivo = '../Data/precios.csv'):
  """Mostrar el precio de venta de los cajones en el negocio.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.

  Ejemplo:
    >>> leer_precios('../Data/precios.csv')[:1]
    [('Acelga', 29.26)]
  """
  return parse_csv(nombre_archivo, types=[str, float], has_headers=False)

#%% Clase03_3.13 - 
def hacer_informe(camion = [], precios = []):
  """Generar un informe.

  Parametros:
    `camion` (list): carga de un camion con el precio de costo.
    `precios` (list): precio de venta de la carga del camion.

  Ejemplo:
    >>> camion = leer_camion('../Data/camion.csv')
    >>> precios = leer_precios('../Data/precios.csv')
    >>> hacer_informe(camion, precios)[:1]
    [('Lima', 100, 32.2, 8.019999999999996)]
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

#%% 6.4 - imprimir la tabla con el informe
def imprimir_informe(informe = []):
  """Imprimir una tabla con datos del informe.

  Parametros:
    `informe` (list): listado de tuplas.

  Ejemplo:
    >>> camion = leer_camion('../Data/camion.csv')
    >>> precios = leer_precios('../Data/precios.csv')
    >>> informe = hacer_informe(camion, precios)
    >>> imprimir_informe(informe)
    # imprime un cuadro formateado
  """
  cabeceras = ('Nombre', 'Cajones', 'Precio', 'Cambio')
  encabezado = f'%10s %10s %10s %10s' % cabeceras
  separador = ('-' * 10 + ' ') * len(cabeceras)
  print(encabezado)
  print(separador)
  for dato in informe:
    print('%10s %10d %10.2f %10.2f' % dato)
  print()

#%% 6.5 - crear funcion de alto nivel
def informe_camion(nombre_archivo_camion = '../Data/camion.csv', nombre_archivo_precios = '../Data/precios.csv'):
  """Realizar el informe y luego mostrarlo.

  Parametros:
    `nombre_archivo_camion` (str): ruta al archivo csv con datos 
    del precio de costo del camion.
    `nombre_archivo_precios` (str): ruta al archivo csv con datos 
    del precio de venta.

  Ejemplo:
    >>> informe_camion('../Data/camion.csv', '../Data/precios.csv')
    # llama a la funcion imprimir_informe(informe)
    # muestra el cuadro formateado
  """
  camion = leer_camion(nombre_archivo_camion)
  precios = leer_precios(nombre_archivo_precios)
  datos_informe = hacer_informe(camion, precios)
  imprimir_informe(datos_informe)
