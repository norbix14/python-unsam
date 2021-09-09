#!/usr/bin/env python3
# arboles.py

import csv
import numpy as np
import matplotlib.pyplot as plt

######################################################################
"""
@author: Norberto Fabrizio
"""

# 5.5 - Graficos del arbolado porteño.

#%% Clase04_4.15 - leer_arboles(nombre_archivo)
def leer_arboles(nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'):
  """Mostrar toda la informacion de los arboles.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.

  Ejemplo:
    >>> from pprint import pprint
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> arboleda = leer_arboles(nombre_archivo)
    # tener cuidado, ya que mostraria 51502 resultados
    >>> print(len(arboleda))
    51502
    >>> pprint(arboleda[:1])
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
    with open(nombre_archivo, 'rt') as archivo:
      filas = csv.reader(archivo)
      cabeceras = next(filas)
      tipos = [float, float, int, int, int, int, int, str, str,
              str, str, str, str, str, str, float, float]
      arboleda = [
        dict(
          zip(
            cabeceras, 
            [
              func(val)
              for func, val in zip(tipos, fila)
            ]
          )
        )
        for fila in filas
      ]
    return arboleda
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#%% Clase04_4.17 - altos y diametros de los jacaranda
def alturas_diametros_jacaranda(especie = 'Jacarandá', nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'):
  """Mostrar las alturas y diametros de los Jacarandá.

  Parametros:
    `especie` (str): especie del cual obtener los datos.
    `nombre_archivo` (str): ruta al archivo CSV para buscar los arboles.

  Ejemplo:
    >>> from pprint import pprint
    >>> altdiam = alturas_diametros_jacaranda('jacarandá')
    >>> pprint(altdiam[:10])
    # datos como (altura, diametro)
    [(5, 10),
     (5, 10),
     (5, 10),
     (5, 10),
     (5, 10),
     (5, 10),
     (5, 10),
     (5, 10),
     (5, 10),
     (5, 10)]
  """
  arboleda = leer_arboles(nombre_archivo)
  alt_diam_especie = [
    (arbol['altura_tot'], arbol['diametro'])
    for arbol in arboleda
    if (arbol['nombre_com'].lower() == especie.lower())
  ]
  return alt_diam_especie

#%% Clase04_4.18 - medidas_de_especies(especies, arboleda)
def medidas_de_especies(especies = [], arboleda = []):
  """Mostrar las medidas de una especie en la arboleda.

  Parametros:
    `especies` (list): listado de especies.
    `arboleda` (list): lista con informacion de los arboles.

  Ejemplo:
    >>> from pprint import pprint
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    >>> arboleda = leer_arboles(nombre_archivo)
    >>> medidas = medidas_de_especies(especies, arboleda)
    >>> pprint(medidas)
    # se muestra un modelo de lo que devolveria
    # {especie: [(altura, diametro), (h, d)]}
    {'Eucalipto': [(1, 2), (3, 4)],
     'Jacarandá': [(1, 2), (3, 4)],
     'Palo borracho rosado': [(1, 2), (3, 4)]}
  """
  if (type(especies) is list):
    if (len(especies) <= 0):
      return {}
    lista = []
    for especie in especies:
      alt_diam = [
        (arbol['altura_tot'], arbol['diametro'])
        for arbol in arboleda
        if arbol['nombre_com'].lower() == especie.lower()
      ]
      lista.append(alt_diam)
    diccionario = {
      especie: alt_diam
      for especie, alt_diam in zip(especies, lista)
    }
    return diccionario
  return {}

#%% 5.25 - histograma de altos de jacarandas
def histograma_altos_jacaranda(especie = 'jacarandá', nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'):
  """Generar un histograma con las alturas de los Jacarandá.

  Parametros:
    `especie` (str): especie el cual obtener el histograma.
    `nombre_archivo` (str): ruta al dataset del arbolado porteño.

  Ejemplo:
    >>> histograma_altos_jacaranda()
    # mostrar histograma con parametros por defecto
  """
  arboleda = leer_arboles(nombre_archivo)
  alt_especie = [
    arbol['altura_tot']
    for arbol in arboleda
    if (arbol['nombre_com'].lower() == especie.lower())
  ]
  plt.hist(alt_especie, bins=100)
  plt.title('Alturas de los Jacarandá')
  plt.xlabel('Alturas')
  plt.ylabel('Cantidad')
  plt.show()

#%% 5.26 - scatterplot (diametro vs alto) de jacarandas
def scatter_hd(lista_de_pares = [], especie = 'especie'):
  """Generar un scatterplot para visualizar relacion entre altura y diametro.

  Parametros:
    `lista_de_pares` (list): listado con pares de tuplas.
    `especie` (str): especie a mostrar.

  Ejemplo:
    >>> altdiam = alturas_diametros_jacaranda()
    >>> scatter_hd(altdiam)
    # mostrar scatterplot de la especie
  """
  x = []
  y = []
  N = len(lista_de_pares)
  if (N > 0):
    N = len(lista_de_pares)
    # x=d (diametro)
    x = [d for h,d in lista_de_pares]
    # y=h (altura)
    y = [h for h,d in lista_de_pares]
  colors = np.random.rand(N)
  # 0 to 15 point radii
  area = (30 * np.random.rand(N))**2
  xlim = max(x) + 10 if x else 10
  ylim = max(y) + 10 if y else 10
  plt.scatter(x, y, s=area, c=colors, alpha=0.5)
  plt.title(f'Relacion diametro-alto de {especie}')
  plt.xlabel('Diametro (cm)')
  plt.xlim(0, xlim)
  plt.ylabel('Altura (m)')
  plt.ylim(0, ylim)
  plt.show()
  return None

#%% 5.27 - scatterplot para diferentes especies
# eucalipto
def scatterplot_eucalipto(especie = 'eucalipto', archivo = '../Data/arbolado-en-espacios-verdes.csv'):
  """Mostrar scatterplot de la especie provista.

  Parametros:
    `especie` (str): especie a mostrar el scatterplot.
    `archivo` (str): ruta necesaria para buscar todos los arboles.

  Ejemplo:
    >>> scatterplot_eucalipto()
    # muestra el grafico
  """
  arboleda = leer_arboles(archivo)
  medidas = medidas_de_especies([especie], arboleda)
  scatter_hd(medidas[especie], especie)
  return None
# palo borracho rosado
def scatterplot_palo_borracho_rosado(especie = 'palo borracho rosado', archivo = '../Data/arbolado-en-espacios-verdes.csv'):
  """Mostrar scatterplot de la especie provista.

  Parametros:
    `especie` (str): especie a mostrar el scatterplot.
    `archivo` (str): ruta necesaria para buscar todos los arboles.

  Ejemplo:
    >>> scatterplot_palo_borracho_rosado()
    # muestra el grafico
  """
  arboleda = leer_arboles(archivo)
  medidas = medidas_de_especies([especie], arboleda)
  scatter_hd(medidas[especie], especie)
  return None
# jacarandá
def scatterplot_jacaranda(especie = 'jacarandá', archivo = '../Data/arbolado-en-espacios-verdes.csv'):
  """Mostrar scatterplot de la especie provista.

  Parametros:
    `especie` (str): especie a mostrar el scatterplot.
    `archivo` (str): ruta necesaria para buscar todos los arboles.

  Ejemplo:
    >>> scatterplot_jacaranda()
    # muestra el grafico
  """
  arboleda = leer_arboles(archivo)
  medidas = medidas_de_especies([especie], arboleda)
  scatter_hd(medidas[especie], especie)
  return None
# generico
def scatterplot_generico(especie = 'cedro del himalaya', archivo = '../Data/arbolado-en-espacios-verdes.csv'):
  """Mostrar scatterplot de la especie provista.

  Parametros:
    `especie` (str): especie a mostrar el scatterplot.
    `archivo` (str): ruta necesaria para buscar todos los arboles.

  Ejemplo:
    >>> scatterplot_generico('cedro del himalaya')
    # muestra el grafico de la especie provista
  """
  arboleda = leer_arboles(archivo)
  medidas = medidas_de_especies([especie], arboleda)
  scatter_hd(medidas[especie], especie)
  return None
