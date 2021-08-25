#!/usr/bin/env python3
# tablamult.py

######################################################################
"""
@author: Norberto Fabrizio
"""

# 3.17

#%% definicion de la funcion
def tablamult():
  """Imprimir las tablas de multiplicar en formato de tabla."""
  # encabezados
  for e in range(10):
    print(f'{e:>4d}', end = '')
  print('\n')
  # separador
  print('{:->42s}'.format('-'))
  # columnas
  for c in range(10):
    print(f'{c}', end = ':')
    # tablas
    op = 0
    for t in range(10):
      op += c if t != 0 else 0
      fila = f'{op:>4d}'
      print(fila, end = '')
    print('\n')

#%% ver tabla de multiplicar
if __name__ == '__main__':
  tablamult()
