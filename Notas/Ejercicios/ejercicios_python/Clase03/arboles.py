#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# arboles.py
"""
@author: Norberto Fabrizio
"""

import csv

from collections import Counter

#%% 3.18 - funcion leer_parque(nombre_archivo, parque)
def leer_parque(nombre_archivo, parque):
  """Mostrar toda la informacion de cada arbol que hay en el parque.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.
    `parque` (str): parque en donde buscar los arboles.

  Ejemplo:
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    >>> lista_arboles[:1]
    [{'altura_tot': '20',
      'coord_x': '96164.756178',
      'coord_y': '106842.46540700001',
      'diametro': '33',
      'espacio_ve': 'GENERAL PAZ',
      'id_arbol': '1380',
      'id_especie': '330',
      'inclinacio': '5',
      'lat': '-34.5675817714',
      'long': '-58.5050933042',
      'nombre_cie': 'Eucalyptus sp.',
      'nombre_com': 'Eucalipto',
      'nombre_fam': 'Mirtáceas',
      'nombre_gen': 'Eucalyptus',
      'origen': 'Exótico',
      'tipo_folla': 'Árbol Latifoliado Perenne',
      'ubicacion': 'LARRALDE, CRISOLOGO, AV. - PAZ, GRAL., AV.- AIZPURUA'}]
  """
  try:
    lista = []
    errores = 0
    with open(nombre_archivo, 'rt', encoding='UTF-8') as archivo:
      filas = csv.reader(archivo)
      cabeceras = next(filas)
      for fila in filas:
        try:
          arbol = dict(zip(cabeceras, fila))
          if (arbol['espacio_ve'].lower() == parque.lower()):
            lista.append(arbol)
        except:
          errores += 1
    return lista
  except FileNotFoundError:
    print(f'No existe el archivo o carpeta "{nombre_archivo}".')
    return []

#%% 3.19 - funcion especies(lista_arboles)
def especies(lista_arboles):
  """Mostrar todas las especies de arboles que hay en la lista de forma unica.

  Parametros:
    `lista_arboles` (list): listado de arboles.

  Ejemplo:
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    >>> especies(lista_arboles)
    # se muestran algunos elementos a modo de ejemplo
    {'Limpiatubos', 'Roble', 'Tuja', 'Acacia negra', 'Pino de las canarias'}
  """
  lista = []
  for fila in lista_arboles:
    try:
      lista.append(fila['nombre_com'])
    except:
      pass
  return set(lista)

#%% 3.20 - funcion contar_ejemplares(lista_arboles)
def contar_ejemplares(lista_arboles):
  """Contar cuantos ejemplares de cada arbol hay en la lista.

  Parametros:
    `lista_arboles` (list): listado de arboles.

  Ejemplo:
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    >>> ejemplares = contar_ejemplares(lista_arboles)
    >>> ejemplares
    # se muestran algunos elementos a modo de ejemplo
    Counter({'Casuarina': 97, 'Tipa blanca': 54, 'Eucalipto': 49})
    >>> ejemplares.most_common(2)
    [('Casuarina', 97), ('Tipa blanca', 54)]
  """
  ejemplares = Counter()
  for fila in lista_arboles:
    try:
      ejemplares[fila['nombre_com']] += 1
    except:
      pass
  return ejemplares

#%% 3.21 - funcion obtener_alturas(lista_arboles, especie)
def obtener_alturas(lista_arboles, especie):
  """Mostrar todas las alturas de la especie en la lista.

  Parametros:
    `lista_arboles` (list): listado de arboles.
    `especie` (str): especie del arbol.

  Ejemplo:
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    >>> obtener_alturas(lista_arboles, 'Jacarandá')[:10]
    [10.0, 10.0, 10.0, 13.0, 10.0, 14.0, 13.0, 8.0, 8.0, 13.0]
  """
  lista = []
  for fila in lista_arboles:
    try:
      if (fila['nombre_com'].lower() == especie.lower()):
        lista.append(float(fila['altura_tot']))
    except:
      pass
  return lista

#%% 3.22 - funcion obtener_inclinaciones(lista_arboles, especie)
def obtener_inclinaciones(lista_arboles, especie):
  """Mostrar todas las inclinaciones de la especie en la lista.

  Parametros:
    `lista_arboles` (list): listado de arboles.
    `especie` (str): especie del arbol.

  Ejemplo:
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    >>> obtener_inclinaciones(lista_arboles, 'Jacarandá')[:10]
    [0.0, 25.0, 25.0, 17.0, 0.0, 13.0, 0.0, 6.0, 13.0, 11.0]
  """
  lista = []
  for fila in lista_arboles:
    try:
      if (fila['nombre_com'].lower() == especie.lower()):
        lista.append(float(fila['inclinacio']))
    except:
      pass
  return lista

#%% 3.23 - funcion especimen_mas_inclinado(lista_arboles)
def especimen_mas_inclinado(lista_arboles):
  """Mostrar que ejemplar es el mas inclinado y su inclinacion en la lista.

  Parametros:
    `lista_arboles` (list): listado de arboles.

  Ejemplo:
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'centenario')
    >>> especimen_mas_inclinado(lista_arboles)
    {'ejemplar': 'Falso Guayabo (Guayaba del Brasil)', 'inclinacion': 80.0}
  """
  especies_unicas = especies(lista_arboles)
  inclinaciones = [
    (max(obtener_inclinaciones(lista_arboles, especie)), especie)
    for especie in especies_unicas
  ]
  cabeceras = ('inclinacion', 'ejemplar')
  if (len(inclinaciones) > 0):
    inclinacion, ejemplar = max(inclinaciones)
  else:
    inclinacion, ejemplar = 0.0, 0.0
  emi = (inclinacion, ejemplar)
  return dict(zip(cabeceras, emi))

#%% 3.24 - funcion especie_promedio_mas_inclinada(lista_arboles)
def especie_promedio_mas_inclinada(lista_arboles):
  """Mostrar la especie que en promedio tiene la mayor inclinacion.

  Parametros:
    `lista_arboles` (list[tuple]): listado de tuplas.

  Ejemplo:
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'andes, los')
    >>> especie_promedio_mas_inclinada(lista_arboles)
    {'ejemplar': 'Álamo Plateado', 'inclinacion_promedio': 25.0}
  """
  especies_unicas = especies(lista_arboles)
  lista_inclinaciones = []
  for especie in especies_unicas:
    inclinaciones = obtener_inclinaciones(lista_arboles, especie)
    promedio = sum(inclinaciones) / len(inclinaciones)
    lista_inclinaciones.append((promedio, especie))
  cabeceras = ('inclinacion_promedio', 'ejemplar')
  if (len(lista_inclinaciones) > 0):
    inclinacion, ejemplar = max(lista_inclinaciones)
  else:
    inclinacion, ejemplar = 0.0, 0.0
  epmi = (inclinacion, ejemplar)
  return dict(zip(cabeceras, epmi))

#%% helper max_prom(lista)
def max_prom(lista):
  """Ver la altura maxima y calcular el promedio.

  Parametros:
    `lista` (list): listado de numeros.

  Ejemplo:
    >>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> max_prom(lista)
    {'maxima': 9.0, 'promedio': 5.0}
  """
  cabeceras = ('maxima', 'promedio')
  alturas = (float(max(lista)), round(sum(lista) / len(lista), 2))
  informe = dict(zip(cabeceras, alturas))
  return informe

#%%
def main():
  """Testear todas las funciones segun lo que piden los ejercicios.

  Ejemplo:
    >>> python3 arboles.py > resultados.txt
    # ejecutar el test
    # guardar el resultado en un archivo de texto
  """
  nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
  parques = ['general paz', 'andes, los', 'centenario']
  for parque in parques:
    lista_arboles = leer_parque(nombre_archivo, parque)

    # 3.18 - Lectura de los arboles en el parque
    print(f'Arboles en <{parque}>: {len(lista_arboles)}')

    # 3.19 - Determinar las especies en un parque
    print(f'Especies unicas en <{parque}>')
    print(especies(lista_arboles))

    # 3.20 - Contar ejemplares por especie
    print(f'Los 5 ejemplares mas comunes en <{parque}>')
    print(contar_ejemplares(lista_arboles).most_common(5))

    # 3.21 - Alturas de una especie en una lista
    print(f'Alturas de <Jacarandá> en <{parque}>')
    print(max_prom(obtener_alturas(lista_arboles, 'Jacarandá')))

    # 3.22 - Inclinaciones por especie de una lista
    print(f'Inclinaciones de <Jacarandá> en <{parque}>')
    print(obtener_inclinaciones(lista_arboles, 'Jacarandá'))

    # 3.23 - Especie con el ejemplar mas inclinado
    print(f'Ejemplar mas inclinado en <{parque}>')
    print(especimen_mas_inclinado(lista_arboles))

    # 3.24 - Especie mas inclinada en promedio
    print(f'Ejemplar que en promedio tiene mayor inclinacion en <{parque}>')
    print(especie_promedio_mas_inclinada(lista_arboles))

    print('\n')
