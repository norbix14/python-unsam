#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tests.py
"""
@author: Norberto Fabrizio
"""

import os

import csv

from vigilante import vigilar, filematch

from informe_final import leer_camion

from ticker import filtrar_datos, parsear_datos, ticker

from lote import Lote

from camion import Camion

from listar_imgs import archivos_png

#%% 10.7 - 
def ej_107():
  directorio = 'Data'
  mercado_csv = 'mercadolog.csv'
  camion_csv = 'camion.csv'

  archivo_camion = os.path.join('..', directorio, camion_csv)
  archivo_mercado = os.path.join('..', directorio, mercado_csv)

  with open(archivo_camion, 'rt', encoding='UTF-8') as f:
    camion = leer_camion(f)
    for line in vigilar(archivo_mercado):
      fields = line.split(',')
      nombre = fields[0].strip('"')
      precio = float(fields[1])
      volumen = int(fields[2])
      if nombre in camion:
        print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')

#%% 10.8
def ej_108():
  directorio = 'Data'
  mercado_csv = 'mercadolog.csv'
  archivo_mercado = os.path.join('..', directorio, mercado_csv)

  lines = vigilar(archivo_mercado)
  naranjas = filematch(lines, 'Naranja')
  for n in naranjas:
    print(n)

#%% 10.9
def ej_109():
  directorio = 'Data'
  mercado_csv = 'mercadolog.csv'
  archivo_mercado = os.path.join('..', directorio, mercado_csv)

  lines = vigilar(archivo_mercado)
  filas = csv.reader(lines)
  for fila in filas:
    print(fila)

#%% 10.10
def ej_1010():
  directorio = 'Data'
  mercado_csv = 'mercadolog.csv'
  archivo_mercado = os.path.join('..', directorio, mercado_csv)

  lines = vigilar(archivo_mercado)
  rows = parsear_datos(lines)
  for row in rows:
    print(row)

#%% 10.11
def ej_1011():
  directorio = 'Data'
  camion_csv = 'camion.csv'
  mercado_csv = 'mercadolog.csv'

  archivo_mercado = os.path.join('..', directorio, mercado_csv)
  archivo_camion = os.path.join('..', directorio, camion_csv)

  with open(archivo_camion, 'rt', encoding='UTF-8') as f:
    camion = leer_camion(f)
    rows = parsear_datos(vigilar(archivo_mercado))
    rows = filtrar_datos(rows, camion)
    for row in rows:
      print(row)

#%% 10.12
def ej_1012(archivo = 'camion', formato = 'txt'):
  directorio = 'Data'
  camion_csv = f'{archivo}.csv'
  mercado_csv = 'mercadolog.csv'

  archivo_mercado = os.path.join('..', directorio, mercado_csv)
  archivo_camion = os.path.join('..', directorio, camion_csv)  

  ticker(archivo_camion, archivo_mercado, formato)

#%% 10.14
def ej_1014():
  camion = Camion([
    Lote('Albaca', 100, 200.54),
    Lote('Remolacha', 230, 128.54),
    Lote('Espinaca', 301, 231.54),
    Lote('Chaucha', 219, 234.54)
  ])
  for c in camion:
    print(c)
  return camion

#%% 10.16
def ej_1016(archivo = 'ordenar_clon'):
  directorio = 'Data'
  archivo_csv = f'{archivo}.csv'
  ruta = os.path.join('..', directorio, archivo_csv)
  png = archivos_png(ruta)
  return png
