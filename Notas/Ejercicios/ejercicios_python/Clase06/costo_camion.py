#!/usr/bin/env python3
# costo_camion.py

import informe_funciones

######################################################################
"""
@author: Norberto Fabrizio
"""

# 3.9

#%% Clase03_3.9 - 
def costo_camion(nombre_archivo = '../Data/camion.csv'):
  """Calcular el costo total pagado por los cajones.

  Parametros:
    `nombre_archivo` (str): ruta al archivo csv.

  Ejemplo:
    >>> costo_camion()
    47671.15
    >>> costo_camion('../Data/camion2.csv')
    19908.75
    >>> costo_camion('../Data/missing.csv')
    30381.15
    >>> costo_camion('../Data/camion_blancos.csv')
    47671.15
  """
  camion = informe_funciones.leer_camion(nombre_archivo)
  return sum([
    producto['cajones'] * producto['precio']
    for producto in camion
  ])
