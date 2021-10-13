#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lote.py
"""
@author: Norberto Fabrizio
"""

# 9.2 - Clases
# 9.1 - Objetos como estructura de datos
# 9.4 - Metodos especiales

#%% 9.1, 9.2, 9.9 - 
class Lote():
  """Clase Lote para manejar carga de un camion."""
  def __init__(self, nombre, cajones, precio) -> None:
    """Crear un nuevo lote con datos del producto.

    Parametros:
      `nombre` (str): nombre del producto.
      `cajones` (int): cantidad de cajones del producto.
      `precio` (float): precio del cajon del producto.
    """
    self.nombre = nombre
    self.cajones = cajones
    self.precio = precio

  def __repr__(self) -> str:
    return f'Lote("{self.nombre}", {self.cajones}, {self.precio})'

  def costo(self):
    """Calcular el costo del cajon."""
    return self.cajones * self.precio

  def vender(self, cantidad):
    """Vender cajones.

    Parametros:
      `cantidad` (int): cantidad de cajones a vender.
    """
    if (cantidad > self.cajones):
      raise ValueError('La cantidad a querer vender es mayor al stock actual.')
    self.cajones -= cantidad
