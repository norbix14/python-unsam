#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clases.py
"""
@author: Norberto Fabrizio
"""

import os

import datetime

import time

# 8.3 - Manejo de archivos y carpetas
# 8.4 - Ordenar archivos en Python

#%% manejo de archivos y directorios

#%% obtener el directorio actual

#%% cambiar el directorio de trabajo

#%% listar directorios y archivos

#%% crear un nuevo directorio

#%% renombrar un directorio o un archivo

#%% eliminar un directorio o un archivo

#%% recorriendo directorios con os.walk()
def recorrer_directorio(directorio):
  """Recorrer en busca de png."""
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

#%% cambiar atributos de un archivo
def cambiar_atributos(archivo):
  """Cambiar los atributos del archivo."""
  stats_archivo = os.stat(archivo)
  print(time.ctime(stats_archivo.st_atime))

  fecha_acceso = datetime.datetime(
    year=2021, month=7, day=25,
    hour=14, minute=14, second=14
  )
  fecha_modif = datetime.datetime(
    year=2021, month=7, day=25,
    hour=16, minute=16, second=16
  )

  ts_acceso = fecha_acceso.timestamp()
  ts_modif = fecha_modif.timestamp()
  os.utime(archivo, (ts_acceso, ts_modif))

  stats_archivo = os.stat(archivo)
  print(time.ctime(stats_archivo.st_atime))

#%%
if __name__ == '__main__':
  archivo = '../Data/ordenar_clon'
  print(recorrer_directorio(archivo))
