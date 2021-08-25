#!/usr/bin/env python3
# arboles.py

import csv
from collections import Counter
from pprint import pprint

######################################################################
"""
@author: Norberto Fabrizio
"""

#%% 3.18 - funcion leer_parque(nombre_archivo, parque)
def leer_parque(nombre_archivo, parque):
  """Mostrar toda la informacion de cada arbol que hay en el parque.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.
    `parque` (str): parque en donde buscar los arboles.

  Ejemplo:
    >>> from pprint import pprint
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    # tener cuidado, ya que mostraria 690 resultados
    >>> print(len(lista_arboles))
    690
    >>> pprint(lista_arboles)
    # se muestra un elemento a modo de ejemplo
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
  lista = []
  errores = 0
  try:
    with open(nombre_archivo, 'rt') as archivo:
      filas = csv.reader(archivo)
      cabeceras = next(filas)
      try:
        for i, fila in enumerate(filas, start = 0):
          arbol = dict(zip(cabeceras, fila))
          if (arbol['espacio_ve'].lower() == parque.lower()):
            lista.append(arbol)
      except ValueError:
        errores += 1
      except IndexError:
        errores += 1
    return lista
  except FileNotFoundError:
    return 'No existe el archivo o carpeta'

#%% 3.19 - funcion especies(lista_arboles)
def especies(lista_arboles):
  """Mostrar todas las especies de arboles que hay en la lista
  de forma unica.

  Parametros:
    `lista_arboles` (list): listado de arboles.

  Ejemplo:
    >>> from pprint import pprint
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    >>> especies_unicas = especies(lista_arboles)
    >>> print(len(especies_unicas))
    81
    >>> pprint(especies_unicas)
    # se muestran algunos elementos a modo de ejemplo
    {'Acacia blanca',
     'Acacia negra',
     'Alcanforero',
     'Arce negundo',
     'Bunya-bunya (Araucaria de Bidwill)',
     'Caqui',
     'Casuarina',
     'Cedrela',
     'Cedro',
     'Cedro de San Juan',
     'Cedro del Atlas (Cedro plateado o Cedro atlántico)',
     'Cedro del Himalaya',
     'Cedro del Himalaya variedad aurea',
     'Ceibo'}
  """
  lista = []
  for i, fila in enumerate(lista_arboles, start = 0):
    lista.append(fila['nombre_com'])
  return set(lista)

#%% 3.20 - funcion contar_ejemplares(lista_arboles)
def contar_ejemplares(lista_arboles):
  """Contar cuantos ejemplares de cada arbol hay en la lista.

  Parametros:
    `lista_arboles` (list): listado de arboles.

  Ejemplo:
    >>> from pprint import pprint
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    >>> ejemplares = contar_ejemplares(lista_arboles)
    >>> pprint(ejemplares.most_common(5))
    # ver los 5 resultados mas comunes
    [('Casuarina', 97),
     ('Tipa blanca', 54),
     ('Eucalipto', 49),
     ('Palo borracho rosado', 44),
     ('Fenix', 40)]
    >>> pprint(ejemplares)
    # se muestran algunos elementos a modo de ejemplo
    Counter({'Casuarina': 97,
             'Tipa blanca': 54,
             'Eucalipto': 49,
             'Palo borracho rosado': 44,
             'Fenix': 40,
             'Ciprés': 33,
             'Plátano': 31,
             'Morera blanca': 22,
             'Cedro del Himalaya': 22,
             'Jacarandá': 20,
             'Fresno americano': 19,
             'Arce negundo': 16,
             'Washingtonia': 13,
             'Bunya-bunya (Araucaria de Bidwill)': 12})
  """
  ejemplares = Counter()
  for i, fila in enumerate(lista_arboles, start = 0):
    ejemplares[fila['nombre_com']] += 1
  return ejemplares

#%% 3.21 - funcion obtener_alturas(lista_arboles, especie)
def obtener_alturas(lista_arboles, especie):
  """Mostrar todas las alturas de la especie en la lista.

  Parametros:
    `lista_arboles` (list): listado de arboles.
    `especie` (str): especie del arbol.

  Ejemplo:
    >>> from pprint import pprint
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    >>> alt_jac_gpaz = obtener_alturas(lista_arboles, 'Jacarandá')
    >>> pprint(alt_jac_gpaz)
    # se muestran algunos elementos a modo de ejemplo
    [10.0,
     10.0,
     10.0,
     13.0,
     10.0,
     14.0,
     13.0,
     8.0,
     8.0,
     13.0]
  """
  lista = []
  for i, fila in enumerate(lista_arboles, start = 0):
    if (fila['nombre_com'].lower() == especie.lower()):
      lista.append(float(fila['altura_tot']))
  return lista

#%% 3.22 - funcion obtener_inclinaciones(lista_arboles, especie)
def obtener_inclinaciones(lista_arboles, especie):
  """Mostrar todas las inclinaciones de la especie en la lista.

  Parametros:
    `lista_arboles` (list): listado de arboles.
    `especie` (str): especie del arbol.

  Ejemplo:
    >>> from pprint import pprint
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'general paz')
    >>> inc_jac_gpaz = obtener_inclinaciones(lista_arboles, 'Jacarandá')
    >>> pprint(inc_jac_gpaz)
    # se muestran algunos elementos a modo de ejemplo
    [0.0,
     25.0,
     25.0,
     17.0,
     0.0,
     13.0,
     0.0,
     6.0,
     13.0]
  """
  lista = []
  for i, fila in enumerate(lista_arboles, start = 0):
    if (fila['nombre_com'].lower() == especie.lower()):
      lista.append(float(fila['inclinacio']))
  return lista

#%% 3.23 - funcion especimen_mas_inclinado(lista_arboles)
def especimen_mas_inclinado(lista_arboles):
  """Mostrar que ejemplar es el mas inclinado y cual es su
  inclinacion en la lista.

  Parametros:
    `lista_arboles` (list): listado de arboles.

  Ejemplo:
    >>> from pprint import pprint
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'centenario')
    >>> especies_unicas = especies(lista_arboles)
    >>> lista_inclinaciones = []
    >>> for especie in especies_unicas:
    ...   max_inc = max(obtener_inclinaciones(lista_arboles, especie))
    ...   inclinacion_especie = (max_inc, especie)
    ...   lista_inclinaciones.append(inclinacion_especie)
    ...
    >>> emi = especimen_mas_inclinado(lista_inclinaciones)
    >>> pprint(emi)
    {'ejemplar': 'Falso Guayabo (Guayaba del Brasil)',
     'inclinacion': 80.0}
  """
  cabeceras = ('inclinacion', 'ejemplar')
  inclinacion, ejemplar = max(lista_arboles)
  emi = (inclinacion, ejemplar)
  return dict(zip(cabeceras, emi))

#%% 3.24 - funcion especie_promedio_mas_inclinada(lista_arboles)
def especie_promedio_mas_inclinada(lista_arboles):
  """Mostrar la especie que en promedio tiene la mayor 
  inclinacion.

  Parametros:
    `lista_arboles` (list): listado de arboles.

  Ejemplo:
    >>> from pprint import pprint
    >>> nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    >>> lista_arboles = leer_parque(nombre_archivo, 'andes, los')
    >>> especies_unicas = especies(lista_arboles)
    >>> lista_inclinaciones = []
    >>> for especie in especies_unicas:
    ...   inclinaciones = obtener_inclinaciones(lista_arboles, especie)
    ...   promedio = sum(inclinaciones) / len(inclinaciones)
    ...   inclinacion_promedio_especie = (promedio, especie)
    ...   lista_inclinaciones.append(inclinacion_promedio_especie)
    ...
    >>> epmi = especie_promedio_mas_inclinada(lista_inclinaciones)
    >>> pprint(epmi)
    {'ejemplar': 'Álamo Plateado',
     'inclinacion_promedio': 25.0}
  """
  cabeceras = ('inclinacion_promedio', 'ejemplar')
  inclinacion, ejemplar = max(lista_arboles)
  epmi = (inclinacion, ejemplar)
  return dict(zip(cabeceras, epmi))

#%% helper max_prom(lista)
def max_prom(lista):
  """Ver la altura maxima y calcular el promedio.

  Parametros:
    `lista` (list): listado de numeros.

  Ejemplo:
    >>> lista = [1,2,3,4,5,6,7,8,9]
    >>> ver_max_prom = max_prom(lista)
    >>> print(ver_max_prom)
    {'maxima': 9, 'promedio': 5}
  """
  cabeceras = ('maxima', 'promedio')
  alturas = (max(lista), round(sum(lista) / len(lista), 2))
  informe = dict(zip(cabeceras, alturas))
  return informe

#%% FUNCION PARA TESTEAR TODAS LAS FUNCIONES
def testear_todo():
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
    especies_unicas = especies(lista_arboles)
    print(f'Especies unicas en <{parque}>')
    pprint(especies_unicas)
    # 3.20 - Contar ejemplares por especie
    ejemplares = contar_ejemplares(lista_arboles)
    print(f'Los 5 ejemplares mas comunes en <{parque}>')
    pprint(ejemplares.most_common(5))
    # 3.21 - Alturas de una especie en una lista
    alturas = obtener_alturas(lista_arboles, 'Jacarandá')
    max_y_prom = max_prom(alturas)
    print(f'Alturas de <Jacarandá> en <{parque}>')
    pprint(max_y_prom)
    # 3.22 - Inclinaciones por especie de una lista
    inclinaciones = obtener_inclinaciones(lista_arboles, 'Jacarandá')
    print(f'Inclinaciones de <Jacarandá> en <{parque}>')
    pprint(inclinaciones)
    #%% 3.23 y 3.24 - Inclinaciones
    lista_inclinaciones = [
      (obtener_inclinaciones(lista_arboles, especie), especie)
      for especie in especies_unicas
    ]
    # 3.23 - Especie con el ejemplar mas inclinado
    listado_emi = [
      (max(inclinaciones), especie)
      for inclinaciones, especie in lista_inclinaciones
    ]
    emi = especimen_mas_inclinado(listado_emi)
    print(f'Ejemplar mas inclinado en <{parque}>')
    pprint(emi)
    # 3.24 - Especie mas inclinada en promedio
    listado_epmi = [
      (sum(inclinaciones) / len(inclinaciones), especie)
      for inclinaciones, especie in lista_inclinaciones
    ]
    epmi = especie_promedio_mas_inclinada(listado_epmi)
    print(f'Ejemplar que en promedio tiene mayor inclinacion en <{parque}>')
    pprint(epmi)
    print('\n')

#%% ejecutar test
testear_todo()
