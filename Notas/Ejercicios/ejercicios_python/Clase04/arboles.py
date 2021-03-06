#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# arboles.py
"""
@author: Norberto Fabrizio
"""

import csv

# 4.5

#%% 4.15 - leer_arboles(nombre_archivo)
def leer_arboles(nombre_archivo):
  """Mostrar toda la informacion de los arboles.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.

  Ejemplo:
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> arboleda = leer_arboles(nombre_archivo)
    >>> len(arboleda)
    51502
    >>> arboleda[:1]
    [{'altura_tot': 6,
      'coord_x': 98692.30571900001,
      'coord_y': 98253.300738,
      'diametro': 35,
      'espacio_ve': 'AVELLANEDA, NICOLÁS, Pres.',
      'id_arbol': 1,
      'id_especie': 53,
      'inclinacio': 0,
      'lat': -34.6450145297,
      'long': -58.4775636069,
      'nombre_cie': 'Washingtonia filifera',
      'nombre_com': 'Washingtonia (Palmera washingtonia)',
      'nombre_fam': 'Arecaceas',
      'nombre_gen': 'Washingtonia',
      'origen': 'Exótico',
      'tipo_folla': 'Palmera',
      'ubicacion': 'DIRECTORIO, AV. - LACARRA, AV. - MONTE -  AUTOPISTA PERITO '
                  'MORENO (AU 6) - AMEGHINO, FLORENTINO, DR.'}]
  """
  try:
    with open(nombre_archivo, 'rt', encoding='UTF-8') as archivo:
      filas = csv.reader(archivo)
      cabeceras = next(filas)
      tipos = [float, float, int, int, int, int, int, str,
        str, str, str, str, str, str, str, float, float]
      arboleda = [
        dict(zip(cabeceras, [func(val) for func, val in zip(tipos, fila)]))
        for fila in filas
      ]
      return arboleda
  except FileNotFoundError:
    print(f'No existe el archivo o carpeta "{nombre_archivo}".')
    return []

#%% 4.16 - alturas de los jacaranda
def alturas_jacaranda(especie = 'Jacarandá'):
  """Mostrar las alturas de los Jacarandá."""
  nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
  arboleda = leer_arboles(nombre_archivo)
  alt_especie = [
    arbol['altura_tot']
    for arbol in arboleda
    if (arbol['nombre_com'].lower() == especie.lower())
  ]
  return alt_especie

#%% 4.17 - altos y diametros de los jacaranda
def alturas_diametros_jacaranda(especie = 'Jacarandá'):
  """Mostrar las alturas y diametros de los Jacarandá."""
  nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
  arboleda = leer_arboles(nombre_archivo)
  alt_diam_especie = [
    (arbol['altura_tot'], arbol['diametro'])
    for arbol in arboleda
    if (arbol['nombre_com'].lower() == especie.lower())
  ]
  return alt_diam_especie

#%% 4.18 - medidas_de_especies(especies, arboleda)
def medidas_de_especies(especies = [], arboleda = []):
  """Mostrar las medidas de una especie en la arboleda.

  Parametros:
    `especies` (list): listado de especies.
    `arboleda` (list): lista con informacion de los arboles.

  Ejemplo:
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    >>> arboleda = leer_arboles(nombre_archivo)
    >>> medidas_de_especies(especies, arboleda)
    # se muestran cuantos elementos tendria cada especie
    {'Eucalipto': 4112, 'Jacarandá': 3255, 'Palo borracho rosado': 3150}
  """
  if (len(arboleda) <= 0):
    return {}
  lista = []
  diccionario = {}
  for especie in especies:
    try:
      alt_diam = [
        (arbol['altura_tot'], arbol['diametro'])
        for arbol in arboleda
        if arbol['nombre_com'].lower() == especie.lower()
      ]
      ###########################
      # MODIFICAR ESTA PARTE LUEGO.
      # DEBE AGREGARSE LA TUPLA CON LAS MEDIDAS.
      # SOLO SE AGREGA LA LONGITUD A MODO DE PRUEBA.
      lista.append(len(alt_diam))
      ###########################
      diccionario = {
        especie: alt_diam
        for especie, alt_diam in zip(especies, lista)
      }
    except:
      pass
  return diccionario

#%%
def main():
  """Main. Ejecutar algunas pruebas."""
  nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
  especie = 'Jacarandá'
  arboleda = leer_arboles(nombre_archivo)
  # 4.16
  alt_especie = [
    arbol['altura_tot']
    for arbol in arboleda
    if (arbol['nombre_com'].lower() == especie.lower())
  ]
  # 4.17
  alt_diam_especie = [
    (arbol['altura_tot'], arbol['diametro'])
    for arbol in arboleda
    if (arbol['nombre_com'].lower() == especie.lower())
  ]
  # resultados
  r_a = len(alt_especie)
  r_a_d = len(alt_diam_especie)
  print(f'{r_a} registros para alturas de {especie}')
  print(f'{r_a_d} registros para alturas y diametros de {especie}')
