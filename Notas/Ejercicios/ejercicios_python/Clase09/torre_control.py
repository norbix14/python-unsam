#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# torre_control.py
"""
@author: Norberto Fabrizio
"""

# 9.5 - Objetos, pilas y colas
# 9.12 - Torre de control

#%% 9.12 - 
#
class Cola:
  """Representa a una cola, con operaciones de encolar y desencolar.
  El primero en ser encolado es tambien el primero en ser desencolado.
  """
  def __init__(self):
    """Crear una cola `items` vacia."""
    self.items = []

  def encolar(self, x):
    """Encolar el elemento `x`."""
    self.items.append(x)

  def desencolar(self):
    """Eliminar el primer elemento de la cola y devolver su valor.
    Si la cola esta vacia, levanta `ValueError`."""
    if (self.esta_vacia()):
      raise ValueError('La cola esta vacia')
    return self.items.pop(0)

  def esta_vacia(self):
    """Devolver `True` si la cola esta vacia, sino `False`."""
    return len(self.items) == 0
#
class TorreDeControl(Cola):
  """Trabajos de una torre de control en un aeropuerto."""
  def __init__(self):
    super().__init__()
    self.arribos = []

  def nueva_partida(self, vuelo):
    """Agregar un nuevo `vuelo`.

    Parametros:
      `vuelo` (str): vuelo en espera de partir.
    """
    super().encolar(vuelo)

  def nuevo_arribo(self, vuelo):
    """Agregar un nuevo arribo el cual tiene prioridad.

    Parametros:
      `vuelo` (str): vuelo en espera de arribar.
    """
    self.arribos.append(vuelo)

  def arribos_vacios(self):
    """Ver si hay arribos pendientes."""
    return len(self.arribos) == 0

  def vaciar_arribos(self):
    """Vaciar los arribos prioritarios."""
    if (self.arribos_vacios()):
      raise ValueError('La cola esta vacia.')
    return self.arribos.pop(0)

  def asignar_pista(self):
    """Asignar la pista a un vuelo con prioridad."""
    if self.arribos_vacios():
      try:
        hay_vuelo = super().desencolar()
        print(f'El vuelo {hay_vuelo} despegó con éxito.')  
      except ValueError:
        print('No hay vuelos en espera.')
    else:
      hay_vuelo = self.vaciar_arribos()
      print(f'El vuelo {hay_vuelo} aterrizó con éxito.')

  def ver_estado(self):
    """Ver el estado general de los vuelos."""
    arribos = 'Ninguno' if self.arribos_vacios() else ', '.join(self.arribos)
    despegues = 'Ninguno' if self.esta_vacia() else ', '.join(self.items)
    print(f'Vuelos esperando para aterrizar: {arribos}')
    print(f'Vuelos esperando para despegar: {despegues}')
