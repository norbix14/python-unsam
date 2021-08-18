#!/usr/bin/env python3
# buscar_precios.py

######################################################################
"""
@author: Norberto Fabrizio
"""

# 2.7

#%% definicion de la funcion
def buscar_precio(nombre_archivo, producto):
  """Buscar el precio del cajon de algun producto.

  Parametros:
    `nombre_archivo` (str): ruta del archivo csv.
    `producto` (str): producto a buscar en la lista.

  Ejemplo:
    >>> naranja = buscar_precio('../Data/precios.csv', 'naranja')
    >>> print(naranja)
    'El cajon de naranja cuesta $106.28'
  """
  resultado = ''
  try:
    with open(nombre_archivo, 'rt') as archivo:
      for linea in archivo:
        fila = linea.split(',')
        nombre = fila[0]
        if (nombre.lower() == producto.lower()):
          precio = fila[1].strip('\n')
          resultado = f'El cajon de {producto} cuesta ${precio}'
          break
        else:
          resultado = f'{producto} no figura en el listado de precios'
    return resultado
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#%% buscar producto
naranja = buscar_precio('../Data/precios.csv', 'naranja')

#%% imprimir resultado
print(naranja)
