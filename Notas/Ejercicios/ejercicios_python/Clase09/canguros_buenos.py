#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# canguros_buenos.py
"""
@author: Norberto Fabrizio
"""

# 9.5 - Objetos, pilas y colas

#%% 9.11 - canguros buenos y canguros malos
class Canguro():
  """Un Canguro es un marsupial."""
  def __init__(self, nombre, contenido=[]):
    """Inicializar los contenidos del marsupio.

    Parametros:
      `nombre` (str): nombre del canguro.
      `contenido` (list): contenido inicial del marsupio.
    """
    self.nombre = nombre
    # * SECCION CORREGIDA
    self.contenido_marsupio = [] if len(contenido) <= 0 else contenido

  def __str__(self):
    """Devolver una representación como cadena de este Canguro."""
    t = [ self.nombre + ' tiene en su marsupio:' ]
    for obj in self.contenido_marsupio:
      s = '    ' + object.__str__(obj)
      t.append(s)
    return '\n'.join(t)

  def meter_en_marsupio(self, item):
    """Agrega un nuevo item al marsupio.

    Parametros:
      `item` (any): objecto a ser agregado.
    """
    self.contenido_marsupio.append(item)

#%%
if __name__ == '__main__':
  madre_canguro = Canguro('Madre')
  cangurito = Canguro('Gurito')
  madre_canguro.meter_en_marsupio('billetera')
  madre_canguro.meter_en_marsupio('llaves del auto')
  madre_canguro.meter_en_marsupio(cangurito)

  print(madre_canguro)
  print(cangurito)
