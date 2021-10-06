#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# listar_imgs.py
"""
@author: Norberto Fabrizio
"""

import sys

import os

# 8.3 - Manejo de archivos y carpetas
# 8.4 - Ordenar archivos en Python

#%% 8.5 - recorrer el arbol de archivos
def archivos_png(directorio):
  """Devolver una lista con todos los archivos png que se encuentren en
  algun directorio/subdirectorio dado.

  Parametros:
    `directorio` (str): nombre del directorio donde buscar los archivos `.png`.

  Ejemplo:
    >>> archivos_png('../Data/ordenar')[:2]
    ['python_20190812.png', 'twitter_bot_20181225.png']

  Última actualización: 01-10-2021 11:30
  """
  try:
    png_files = []
    for root, dirs, files in os.walk(directorio):
      for file in files:
        ext = file.split('.')
        if (ext[len(ext) - 1] == 'png'):
          png_files.append(file)
    return png_files
  except FileNotFoundError:
    print(f'No existe el archivo o carpeta "{directorio}".')
    return []

#%% funcion principal
def f_principal(parametros):
  if (len(parametros) <= 1):
    archivo = parametros[0]
    print('---- Modo de uso ----')
    print(f'{archivo} [a]')
    print('----')
    print('Parametro [a]: nombre del directorio donde comenzar la busqueda.')
    print(f'EJEMPLO: {archivo} ../Data/ordenar')
  else:
    print(archivos_png(parametros[1]))

#%%
if __name__ == '__main__':
  f_principal(sys.argv)
