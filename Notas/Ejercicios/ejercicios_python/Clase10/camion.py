#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# camion.py
"""
@author: Norberto Fabrizio
"""

# 10.2 - El protocolo de iteracion

#%% 10.2, 10.3, 10.14 - 
class Camion():
  def __init__(self, lotes) -> None:
    """Crear un nuevo lote.

    Parametros:
      `lotes` (list): listado de lotes.
    """
    self.lotes = lotes

  def __iter__(self):
    return self.lotes.__iter__()

  def __len__(self):
    return len(self.lotes)

  def __getitem__(self, index):
    return self.lotes[index]

  def __contains__(self, nombre):
    return any([lote.nombre == nombre for lote in self.lotes])

  def __repr__(self) -> str:
    return f'Camion({self.lotes})'

  def __str__(self) -> str:
    print(f'Camion con {len(self.lotes)} lotes:')
    lotes = [
      f"Lote de {l.cajones} cajones de '{l.nombre}', pagados a ${l.precio:0.2f} cada uno."
      for l in self.lotes
    ]
    return '\n'.join(lotes)

  def precio_total(self):
    """Calcular el costo total del lote."""
    return float(sum(l.costo() for l in self.lotes))

  def contar_cajones(self):
    """Contar cuantos cajones de cada producto hay."""
    from collections import Counter
    cantidad_total = Counter()
    for l in self.lotes:
      cantidad_total[l.nombre] += l.cajones
    return cantidad_total
