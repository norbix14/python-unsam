#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ordenar_imgs.py
"""
@author: Norberto Fabrizio
"""

import sys

import os

import datetime

import shutil

# 8.4 - Ordenar archivos en Python

#%%
def archivos_png(directorio):
  """Devolver una lista con todos los archivos .png que se encuentren en
  algun directorio y/o subdirectorio dado.

  Parametros:
    `directorio` (str): nombre del directorio donde buscar los archivos `.png`
    de manera recursiva.

  Ejemplo:
    >>> archivos_png('../Data/ordenar')[:1]
    ['../Data/ordenar/python_20190812.png']

  Última actualización: 02-10-2021 11:00
  """
  try:
    png_files = []
    for root, dirs, files in os.walk(directorio):
      for file in files:
        ext = file.split('.')
        if (ext[len(ext) - 1] == 'png'):
          png_files.append(os.path.join(root, file))
    return png_files
  except FileNotFoundError:
    print(f'No existe el archivo o carpeta "{directorio}".')
    return []

#%% 8.6 - ordenar el arbol de archivos
#
def procesar_nombre(fname):
  """Tomar el nombre del archivo y procesarlo.

  Parametros:
    `fname` (str): nombre del archivo a procesar.

  Ejemplo:
    >>> png_imgs = archivos_png('../Data/ordenar')
    >>> procesar_nombre(png_imgs[0])
    ('../Data/ordenar/imgs/correlation.png', datetime.datetime(2020, 9, 24, 0, 0))
    >>> procesar_nombre('../Data/ordenar/python_20190812.png')
    ('../Data/ordenar/python.png', datetime.datetime(2019, 8, 12, 0, 0))

  Última actualización: 02-10-2021 11:30
  """
  if ((type(fname) is not str) or (not fname)):
    print('Error. El parametro debe ser un string no vacío.')
    return ()
  try:
    dir_data = fname.split('/')
    file_data = dir_data[len(dir_data) - 1]
    root = '/'.join(dir_data[:len(dir_data) - 1])

    file = file_data.split('.')
    ext = file[len(file) - 1]
    img_data = file[0].split('_')

    y = int(img_data[len(img_data) - 1][:4])
    m = int(img_data[len(img_data) - 1][4:6])
    d = int(img_data[len(img_data) - 1][6:8])
    img_date = datetime.datetime(year=y, month=m, day=d)

    img_names = ''.join(img_data[:len(img_data) - 1])
    img = f'{img_names}.{ext}'

    os.rename(fname, os.path.join(root, img))

    return (os.path.join(root, img), img_date)
  except Exception as e:
    print('Error:', e)
    return ()
#
def procesar(fname, destino):
  """Procesar un archivo renombrando, moviendo y modificando su fecha.

  Parametros:
    `fname` (tuple): datos del archivo.
    `destino` (str): destino donde guardar el archivo.

  Ejemplo:
    >>> origen = '../Data/ordenar'
    >>> destino = '../Data/imgs_procesadas'
    >>> imagenes_png = archivos_png(origen)
    >>> datos_imagen = procesar_nombre(imagenes_png[0])
    >>> procesar(datos_imagen, destino)
    # modifica los metadatos, crea el destino si no existe
    # y mueve el archivo al destino elegido

  Última actualización: 02-10-2021 11:30
  """
  if ((type(fname) is not tuple) or (not fname)):
    print('Error. El parametro debe ser una tupla.')
    return
  try:
    file_data = fname[0].split('/')
    root = '/'.join(file_data[:len(file_data) - 1])
    img_name = file_data[len(file_data) - 1]

    img_date = fname[1]

    ts_acceso = img_date.timestamp()
    ts_modif = img_date.timestamp()

    file_origin = os.path.join(root, img_name)

    os.utime(file_origin, (ts_acceso, ts_modif))

    try:
      os.mkdir(destino)
    except FileExistsError:
      pass

    shutil.move(file_origin, destino)
  except Exception as e:
    print('Error:', e)

#%%
def f_principal(parametros):
  """Funcion principal. Ejecuta todas las funciones.

  Parametros:
    `parametros` (list): argumentos que la funcion utilizara. deben ser tres,
    `nombre_script`, `origen` y `destino`.

  Ejemplo:
    >>> f_principal(['ordenar_imgs.py', '../Data/ordenar', '../Data/imgs_procesadas'])
    # busca imagenes png, renombra, modifica metadatos y mueve a otra ubicacion

  última actualización: 06-10-2021 11:00
  """
  args = len(parametros)
  archivo = parametros[0] if args > 0 else 'ordenar_imgs.py'
  if (args <= 1):
    print('---- Modo de uso ----')
    print(f'{archivo} [a] [b]')
    print('----')
    print('Parametro [a]: nombre del directorio donde buscar los archivos.')
    print('Parametro [a]: nombre del directorio donde mover los archivos.')
    print(f'EJEMPLO: {archivo} ../Data/ordenar ../Data/imgs_procesadas')
  else:
    if (args < 3):
      print('Se requieren dos directorios, uno de origen y otro de destino.')
      print(f'EJEMPLO: {archivo} ../Data/ordenar ../Data/imgs_procesadas')
    else:
      origen = parametros[1]
      destino = parametros[2]
      archivos = archivos_png(origen)
      procesados = [
        procesar_nombre(fname)
        for fname in archivos
      ]
      for archivo in procesados:
        procesar(archivo, destino)

#%%
if __name__ == '__main__':
  f_principal(sys.argv)
