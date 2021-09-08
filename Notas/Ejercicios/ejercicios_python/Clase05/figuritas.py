#!/usr/bin/env python3
# figuritas.py

import random
import numpy as np
import matplotlib.pyplot as plt

######################################################################
"""
@author: Norberto Fabrizio
"""

# 5.4 - El album de figuritas

#%% 5.10 - crear un album vacio
def crear_album(figus_total = 6):
  """Crear un album vacio con espacios para pegar figuritas.

  Parametros:
    `figus_total` (int): espacios para pegar las figuritas.

  Ejemplo:
    >>> print(crear_album())
    # por defecto, crea 6 espacios para pegar figuritas
    array([0, 0, 0, 0, 0, 0])
    >>> print(crear_album(10))
    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
  """
  figus_total = int(figus_total)
  return np.zeros(figus_total, dtype=np.int64)

#%% 5.11 - comprobar album incompleto
def album_incompleto(album = []):
  """Comprobar si el album esta completo o incompleto.

  Parametros:
    `album` (list): album a comprobar.

  Ejemplo:
    >>> album = crear_album()
    >>> print(album_incompleto(album))
    True
    >>> print(album_incompleto([1,2,3,4,5,6]))
    False
  """
  if ((type(album) is np.ndarray) or (type(album) is list)):
    return 0 in album
  return False

#%% 5.12 - comprar una figurita individualmente
def comprar_figu(figus_total = 670):
  """Mostrar la figurita que nos toco.

  Parametros:
    `figus_total` (int): rango dentro del cual debe estar la figurita.

  Ejemplo:
    >>> print(comprar_figu(0))
    0
    >>> print(comprar_figu(10))
    8
    >>> print(comprar_figu(670))
    125
  """
  figus_total = int(figus_total)
  if (figus_total <= 0):
    return 0
  return random.randint(1, figus_total)

#%% 5.13 - cuantas figus hay que comprar
def cuantas_figus(figus_total = 10):
  """Calcular cuantas figuritas hay que comprar para completar un album.

  Parametros:
    `figus_total` (int): espacios en el album para las figuritas.

  Ejemplo:
    >>> print(cuantas_figus())
    18
    >>> print(cuantas_figus(90))
    # para un album con 90 espacios, se necesitan 433 figuritas para llenarlo
    433
  """
  figus_total = int(figus_total)
  compras = 0
  album = crear_album(figus_total)
  while album_incompleto(album):
    figuritas = comprar_figu(figus_total)
    album[figuritas - 1] += 1
    compras += 1
  return compras

#%% 5.14 - promedio
def promedio():
  """Calcular cuantas figuritas hay que comprar en promedio
  para completar un album de seis figuritas."""
  cantidad = [
    cuantas_figus(6)
    for _ in range(1000)
  ]
  return np.mean(cantidad)

#%% 5.15 - experimento figuritas
def experimento_figus(n_repeticiones = 10, figus_total = 6):
  """Simular llenado de `n` albumes de `n` figuritas y calcular
  en promedio cuantas se deben comprar para llenarlos.

  Parametros:
    `n_repeticiones` (int): cuantos albumes llenar.
    `figus_total` (int): cantidad de figuritas a llenar en cada album.

  Ejemplo:
    >>> print(experimento_figus())
    14.6
    >>> print(experimento_figus(100, 670))
    4803.93
    >>> print(experimento_figus('10', '6'))
    13.7
    >>> print(experimento_figus(n_repeticiones = 10, figus_total = 6))
    12.6
  """
  n_repeticiones = int(n_repeticiones)
  figus_total = int(figus_total)
  figus = [
    cuantas_figus(figus_total)
    for _ in range(n_repeticiones)
  ]
  return np.mean(figus)

#%% 5.16 - simular generacion de un paquete de 5 figuritas
def simular_generacion_paquete(espacios_album = 670, figus_total = 5):
  """Simular la generacion de un paquete con cinco figuritas.

  Parametros:
    `espacios_album` (int): cuantos espacios hay en el album para las figuritas.
    `figus_total` (int): cuantas figuritas generar en cada paquete.

  Ejemplo:
    >>> print(simular_generacion_paquete())
    [8, 343, 582, 66, 451]
    >>> print(simular_generacion_paquete(100))
    [70, 39, 81, 2, 1]
    >>> print(simular_generacion_paquete('100'))
    [69, 32, 85, 5, 49]
  """
  espacios_album = int(espacios_album)
  figus_total = int(figus_total)
  return [
    random.randint(1, espacios_album)
    for _ in range(figus_total)
  ]

#%% 5.17 - comprar paquete
def comprar_paquete(figus_total = 670, figus_paquete = 6):
  """Generar un paquete de figuritas.

  Parametros:
    `figus_total` (int): espacios en el album para las figuritas.
    `figus_paquete` (int): cuantas figuritas debe tener cada paquete.

  Ejemplo:
    >>> print(comprar_paquete(10))
    [1, 10, 1, 5, 4, 2]
    >>> print(comprar_paquete(10, 10))
    [4, 6, 6, 1, 9, 4, 6, 3, 6, 8]
    >>> print(comprar_paquete(670, 5))
    [294, 629, 250, 543, 176]
  """
  figus_total = int(figus_total)
  figus_paquete = int(figus_paquete)
  return [
    random.randint(1, figus_total)
    for _ in range(figus_paquete)
  ]

#%% 5.18 - cuantos paquetes comprar para completar el album
def cuantos_paquetes(figus_total = 10, figus_paquete = 6):
  """Calcular cuantos paquetes se deben comprar para llenar un album.

  Parametros:
    `figus_total` (int): espacios en el album para las figuritas.
    `figus_paquete` (int): cuantas figuritas debe tener cada paquete.

  Ejemplo:
    >>> print(cuantos_paquetes())
    3
    >>> print(cuantos_paquetes(100))
    86
    >>> print(cuantos_paquetes(100, 5))
    122
    >>> print(cuantos_paquetes(670, 5))
    816
    >>> print(cuantos_paquetes(670, 6))
    621
  """
  figus_total = int(figus_total)
  figus_paquete = int(figus_paquete)
  paquetes = 0
  album = crear_album(figus_total)
  while album_incompleto(album):
    paquete = comprar_paquete(figus_total, figus_paquete)
    while paquete:
      album[paquete.pop() - 1] += 1
    paquetes += 1
  return paquetes

#%% 5.19 - graficar llenado del album
#
def simular_cuantos_paquetes(n_repeticiones = 100):
  """Calcular un promedio de cuantos paquetes comprar para llenar un album.

  Parametros:
    `n_repeticiones` (int): cuantas simulaciones realizar.

  Ejemplo:
    >>> print(simulaciones())
    # en 100 simulaciones
    # se deben comprar, en promedio, 923.66 paquetes
    923.66
    >>> print(simulaciones(100))
    962.44
    >>> print(simulaciones(10))
    953.3
  """
  n_repeticiones = int(n_repeticiones)
  figus_total = 670
  figus_paquete = 5
  lista_paquetes = [
    cuantos_paquetes(figus_total, figus_paquete)
    for _ in range(n_repeticiones)
  ]
  return np.mean(lista_paquetes)
#
def calcular_historia_figus_pegadas(figus_total = 670, figus_paquete = 5):
  """Calcular que figuritas se fueron usando y pegando.

  Parametros:
    `figus_total` (int): espacios en el album para las figuritas.
    `figus_paquete` (int): cuantas figuritas debe tener cada paquete.

  Ejemplo:
    >>> calcular_historia_figus_pegadas()
    # se muestran algunos elementos a modo de ejemplo
    [0, 5, 10, 15, 19, 24, 29, 34, 39, 44, 49, 54, 57, 62, 66, 71, 76, 81, 
     86, 91, 95, 99, 102, 107, 111, 115, 119, 122, 125, 129, 133, 137, 141, 
     146, 148, 153, 156, 160, 162, 164, 167, 172, 173, 178, 182, 185, 187, 
     192, 197, 199, 203, 206, 210, 213, 215, 218, 223, 227, 232, 234, 238, 
     243, 246, 249, 251, 252, 256, 260, 262, 264, 268, 273, 277, 281, 284, 
     288, 290, 293, 293, 296, 300]
  """
  figus_total = int(figus_total)
  figus_paquete = int(figus_paquete)
  album = crear_album(figus_total)
  historia_figus_pegadas = [0]
  while album_incompleto(album):
    paquete = comprar_paquete(figus_total, figus_paquete)
    while paquete:
      album[paquete.pop() - 1] += 1
    figus_pegadas = (album > 0).sum()
    historia_figus_pegadas.append(figus_pegadas)
  return historia_figus_pegadas
#
def graficar_llenado():
  """Graficar la curva de llenado del album de figuritas."""
  figus_total = 670
  figus_paquete = 5
  plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
  plt.xlabel('Cantidad de paquetes comprados.')
  plt.ylabel('Cantidad de figuritas pegadas.')
  plt.title('La curva de llenado se desacelera al final')
  plt.show()

#%% primera simplificacion
def primera_simplificacion():
  figus_total = 6
  album = crear_album(figus_total)
  while album_incompleto(album):
    figurita = comprar_figu(figus_total)
    album[figurita - 1] += 1
  return album

#%% EJERCICIOS OPTATIVOS DE ESTADISTICA.

#%% 5.20 - 


#%% 5.21 - 


#%% 5.22 - 


#%% 5.23 - 


#%% 5.24 - 


