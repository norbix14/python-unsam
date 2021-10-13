#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# informe_final.py
"""
@author: Norberto Fabrizio
"""

import sys

from fileparse import parse_csv

from lote import Lote

from formato_tabla import crear_formateador

from camion import Camion

# 6.2 - Scripting
# 9.2 - Clases
# 9.3 - Herencia
# 10.2 - El protocolo de iteracion

#%% Clase03_3.13, Clase07_7.7, Clase09_9.4, Clase10_10.2 - 
def leer_camion(nombre_archivo):
  """Obtener datos de la carga de un camion.

  Parametros:
    `nombre_archivo` (any): iterable a recorrer.

  Ejemplo:
    >>> nombre_archivo = open('../Data/camion.csv', 'rt', encoding='UTF-8')
    >>> camion = leer_camion(nombre_archivo)
    >>> camion.precio_total()
    47671.15
    >>> camion.contar_cajones()
    Counter({'Mandarina': 250, 'Naranja': 150, 'Caqui': 150, 'Lima': 100, 'Durazno': 95})

  Ultima actualizacion: 12-10-21 22:00
  """
  camion = parse_csv(
    nombre_archivo,
    select=['nombre', 'cajones', 'precio'],
    types=[str, int, float]
  )
  return Camion([Lote(c['nombre'], c['cajones'], c['precio']) for c in camion])

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

#%% Clase03_3.13, Clase09_9.4 - 
def hacer_informe(camion, precios):
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

  Ultima actualizacion: 07-10-21 14:30
  """
  inventario = []
  for producto in camion:
    try:
      cambio = 0.0
      nombre = producto.nombre
      cajones = producto.cajones
      precio = producto.precio
      for producto, precio_venta in precios:
        if (producto == nombre):
          cambio = precio_venta - precio
      tupla = (nombre, cajones, precio, cambio)
      inventario.append(tupla)
    except:
      pass
  return inventario

#%% Clase06_6.4, Clase09_9.5 - 
def imprimir_informe(informe, formateador):
  """Imprimir por pantalla una tabla con datos del informe.

  Parametros:
    `informe` (list): listado de tuplas con el balance entre el costo y la
    ganancia.
    `formateador` (any): objeto con metodos para imprimir por pantalla.

  Ejemplo:
    >>> import formato_tabla

    >>> camion_csv = open('../Data/camion.csv', 'rt', encoding='UTF-8')
    >>> precios_csv = open('../Data/precios.csv', 'rt', encoding='UTF-8')

    >>> camion = leer_camion(camion_csv)
    >>> precios = leer_precios(precios_csv)

    >>> informe = hacer_informe(camion, precios)

    >>> formateador = formato_tabla.FormatoTablaTXT()
    >>> imprimir_informe(informe, formateador)
    # se muestra una tabla formateada por pantalla

  Ultima actualizacion: 07-10-21 17:30
  """
  formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
  for nombre, cajones, precio, cambio in informe:
    formateador.fila([f'{nombre}', f'{cajones}', f'{precio:0.2f}', f'{cambio:0.2f}'])

#%% Clase06_6.5, Clase09_9.5, Clase09_9.6 - 
def informe_camion(nombre_archivo_camion, nombre_archivo_precios, formato = 'txt'):
  """Realizar el informe y luego mostrarlo por pantalla.

  Parametros:
    `nombre_archivo_camion` (any): iterable a recorrer.
    `nombre_archivo_precios` (any): iterable a recorrer.
    `formato` (str): especificar en que formato se quiere ver la tabla.
    por defecto sera en `txt` pero se puede elegir entre `csv` y `html`.

  Ejemplo:
    >>> camion = open('../Data/camion.csv', 'rt', encoding='UTF-8')
    >>> precios = open('../Data/precios.csv', 'rt', encoding='UTF-8')

    >>> informe_camion(camion, precios)
    # realiza el informe y luego muestra una tabla formateada por pantalla

  Ultima actualizacion: 07-10-21 18:30
  """
  formato = formato.lower()
  camion = leer_camion(nombre_archivo_camion)
  precios = leer_precios(nombre_archivo_precios)
  datos_informe = hacer_informe(camion, precios)
  formateador = crear_formateador(formato)
  imprimir_informe(datos_informe, formateador)

#%% Clase07_7.4, Clase09_9.8 - funcion principal
def f_principal(parametros = []):
  """Funcion principal.

  Parametros:
    `parametros` (list): listado de parametros pasados por linea
    de comandos.

  Ultima actualizacion: 07-10-21 19:00
  """
  args = len(parametros)
  file = parametros[0] if args > 0 else 'informe_final.py'
  if (args <= 1):
    print('-- Modo de uso --')
    print(f'{file} [camion_csv] [precios_csv] [formato]')
    print('')
    print('Parametro [camion_csv]: archivo con los datos de los productos.')
    print('Parametro [precios_csv]: archivo con los datos de los precios.')
    print('Parametro [formato]: opcional. especificar el formato de la tabla.')
    print('')
    print(f'EJEMPLO: {file} ../Data/camion.csv ../Data/precios.csv [txt|csv|html]')
  else:
    if (args < 3):
      print('Se requieren dos rutas de dos archivos distintos.')
      print(f'EJEMPLO: {file} ../Data/camion.csv ../Data/precios.csv [txt|csv|html]')
    else:
      formato = parametros[3] if args >= 4 else 'txt'
      camion = open(parametros[1], 'rt', encoding='UTF-8')
      precios = open(parametros[2], 'rt', encoding='UTF-8')
      informe_camion(camion, precios, formato)
      camion.close()
      precios.close()

#%%
if __name__ == '__main__':
  f_principal(sys.argv)
