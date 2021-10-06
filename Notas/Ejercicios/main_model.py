#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file.py
"""
@author: Norberto Fabrizio
"""

import sys

#%% main
def main():
  """Funcion principal."""
  args = sys.argv
  if len(args) <= 1:
    print('---- Modo de uso ----')
    print(f'{args[0]} [a] [b] [c] ...')
    print('----')
    print('Parametro [a]: ')
    print(f'EJEMPLO: {args[0]} ')
    print('----')
    print('Parametro [b]: ')
    print(f'EJEMPLO: {args[0]} ')
  else:
    funciones = []
    n_func = int(args[1])
    aux = 0
    if len(args) > 2:
      aux = args[2]
    try:
      funciones[n_func](aux)
    except IndexError:
      print(f'No hay funcion en el indice {n_func}.')
      print(f'Hay funciones desde el indice 0 al {len(funciones) - 1}')

#%%
if __name__ == '__main__':
  main()
