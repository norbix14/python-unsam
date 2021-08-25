#!/usr/bin/env python3
# tests_arboles.py

from pprint import pprint

import arboles

######################################################################
"""
@author: Norberto Fabrizio
"""

#%% definicion de tests
def test_3_18(parque, lista_arboles = [], listainterna = False):
  """Lectura de los arboles en un parque.

  Debe devolver cuantos arboles hay en el parque especificado.
  """
  if listainterna:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    lista_arboles = arboles.leer_parque(nombre_archivo, parque)
  print(f'Arboles en <{parque}>: {len(lista_arboles)}')

def test_3_19(parque, lista_arboles = [], listainterna = False):
  """Determinar las especies en un parque.

  Debe devolver un conjunto de especies que aparecen en el
  parque. Este conjunto muestra las especies de manera unica,
  sin repetir."""
  if listainterna:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    lista_arboles = arboles.leer_parque(nombre_archivo, parque)
  especies_unicas = arboles.especies(lista_arboles)
  print(f'Especies unicas en <{parque}>')
  pprint(especies_unicas)

def test_3_20(parque, lista_arboles = [], listainterna = False):
  """Contar ejemplares por especie.
  
  Debe devolver las 5 especies mas frecuentes que hay en el
  parque especificado.
  """
  if listainterna:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    lista_arboles = arboles.leer_parque(nombre_archivo, parque)
  ejemplares = arboles.contar_ejemplares(lista_arboles)
  print(f'Los 5 ejemplares mas comunes en <{parque}>')
  pprint(ejemplares.most_common(5))

def test_3_21(parque, especie, lista_arboles = [], listainterna = False):
  """Alturas de una especie en una lista.
  
  Debe calcular la altura promedio y altura maxima de la 
  especie en el parque mencionado.
  """
  if listainterna:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    lista_arboles = arboles.leer_parque(nombre_archivo, parque)
  alturas = arboles.obtener_alturas(lista_arboles, especie)
  max_y_prom = arboles.max_prom(alturas)
  print(f'Alturas de <{especie}> en <{parque}>')
  pprint(max_y_prom)

def test_3_22(parque, especie, lista_arboles = [], listainterna = False):
  """Inclinaciones por especie de una lista.
  
  Debe devolver una lista con todas las inclinaciones
  de la especie en el parque.
  """
  if listainterna:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    lista_arboles = arboles.leer_parque(nombre_archivo, parque)
  inclinaciones = arboles.obtener_inclinaciones(lista_arboles, especie)
  print(f'Inclinaciones de <{especie}> en <{parque}>')
  pprint(inclinaciones)

def test_3_23(parque, lista_arboles = [], listainterna = False):
  """Especie con el ejemplar mas inclinado.

  Debe devolver un diccionario indicando la especie
  con el ejemplar mas inclinado y su inclinacion.
  """
  if listainterna:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    lista_arboles = arboles.leer_parque(nombre_archivo, parque)
  especies_unicas = arboles.especies(lista_arboles)
  lista_inclinaciones = []
  for especie in especies_unicas:
    max_inc = max(arboles.obtener_inclinaciones(lista_arboles, especie))
    lista_inclinaciones.append((max_inc, especie))
  emi = arboles.especimen_mas_inclinado(lista_inclinaciones)
  print(f'Ejemplar mas inclinado en <{parque}>')
  pprint(emi)

def test_3_24(parque, lista_arboles = [], listainterna = False):
  """Especie mas inclinada en promedio.
  
  Debe devolver un diccionario indicando la especie que
  en promedio tiene la mayor inclinacion.
  """
  if listainterna:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    lista_arboles = arboles.leer_parque(nombre_archivo, parque)
  especies_unicas = arboles.especies(lista_arboles)
  lista_inclinaciones = []
  for especie in especies_unicas:
    inclinaciones = arboles.obtener_inclinaciones(lista_arboles, especie)
    promedio = sum(inclinaciones) / len(inclinaciones)
    lista_inclinaciones.append((promedio, especie))
  epmi = arboles.especie_promedio_mas_inclinada(lista_inclinaciones)
  print(f'Ejemplar que en promedio tiene mayor inclinacion en <{parque}>')
  pprint(epmi)

#%% 
if __name__ == '__main__':
  #%% ejecutar todos los tests
  nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
  parques = ['general paz', 'andes, los', 'centenario']
  for parque in parques:
    lista_arboles = arboles.leer_parque(nombre_archivo, parque)
    test_3_18(parque, lista_arboles)
    test_3_19(parque, lista_arboles)
    test_3_20(parque, lista_arboles)
    test_3_21(parque, 'Jacarandá', lista_arboles)
    test_3_22(parque, 'Jacarandá', lista_arboles)
    test_3_23(parque, lista_arboles)
    test_3_24(parque, lista_arboles)
    print('\n')

  #%% ejecutar cada test individualmente
  #test_3_18(parques[0], listainterna = True)
  #test_3_19(parques[0], listainterna = True)
  #test_3_20(parques[0], listainterna = True)
  #test_3_21(parques[0], 'Jacarandá', listainterna = True)
  #test_3_22(parques[0], 'Jacarandá', listainterna = True)
  #test_3_23(parques[0], listainterna = True)
  #test_3_24(parques[0], listainterna = True)
