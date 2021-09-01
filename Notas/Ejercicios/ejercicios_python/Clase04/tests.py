#!/usr/bin/env python3
# tests.py

from pprint import pprint

import busqueda_en_listas as busqueda
import invlista as inversion
import propaga as propagacion
import arboles

######################################################################
"""
@author: Norberto Fabrizio
"""

#%% 4.3, 4.4 - test de busquedas
def test_busquedas():
  b = busqueda
  lista1 = [1,2,3,2,3,4]
  lista2 = [10,2,70,5,10,84,20,30,33,50]
  print(lista1)
  print('index de 1:', b.buscar_u_elemento(lista1, 1))
  print('index de 5:', b.buscar_u_elemento(lista1, 5))
  print('debe dar -1:', b.buscar_u_elemento(123, 1))
  print('debe dar -1:', b.buscar_u_elemento('a1b23d', 1))
  print('debe dar -1:', b.buscar_u_elemento())
  print('veces de 2:', b.buscar_n_elemento(lista1, 2))
  print('veces de 5:', b.buscar_n_elemento(lista1, 5))
  print('debe dar 0:', b.buscar_n_elemento(123, 1))
  print('debe dar 0:', b.buscar_n_elemento('a1b23d', 1))
  print('debe dar 0:', b.buscar_n_elemento())
  print('----')
  print(lista2)
  print('maximo:', b.maximo(lista2))
  print('minimo:', b.minimo(lista2))
  print('----')
  print(b.maximo([1,2,7,2,3,4]))
  print(b.maximo([1,2,3,4]))
  print(b.maximo([-5,4]))
  print(b.maximo([-5,-4]))
  return 0

#%% 4.5 - test de inversion
def test_inversion():
  i = inversion
  lista1 = [1, 2, 3, 4, 5]
  lista2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
  print(lista1)
  print(i.invertir_lista(lista1))
  print('----')
  print(lista2)
  print(i.invertir_lista(lista2))
  print('----')
  print(i.invertir_lista([]))
  return 0

#%% 4.6 - test de propagacion
def test_propagar():
  p = propagacion
  # ejemplos clase
  vector1 = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
  vector2 = [0, 0, 0, 1, 0, 0]
  print('ORIGINAL ', vector1)
  print('PROPAGADO', p.propagar(vector1))
  print('----')
  print('ORIGINAL ', vector2)
  print('PROPAGADO', p.propagar(vector2))
  print('----')
  # ejemplos propios
  vector3 = [-1, -1, 0, 1, 0, -1]
  vector4 = [-1, 1, 0, -1, 0, -1]
  print('ORIGINAL ', vector3)
  print('PROPAGADO', p.propagar(vector3))
  print('----')
  print('ORIGINAL ', vector4)
  print('PROPAGADO', p.propagar(vector4))
  return 0

#%% 4.15 - test de arboles
def test_arboles():
  nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
  especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
  arboleda = arboles.leer_arboles(nombre_archivo)
  medidas = arboles.medidas_de_especies(especies, arboleda)
  alt_jacaranda = [
    arbol['altura_tot']
    for arbol in arboleda
    if (arbol['nombre_com'].lower() == especies[2].lower())
  ]
  r_a = len(alt_jacaranda)
  alt_diam_jacaranda = [
    (arbol['altura_tot'], arbol['diametro'])
    for arbol in arboleda
    if (arbol['nombre_com'].lower() == especies[2].lower())
  ]
  r_a_d = len(alt_diam_jacaranda)
  pprint(arboleda[:1])
  pprint(medidas)
  print(f'{r_a} registros para alturas de {especies[2]}')
  print(f'{r_a_d} registros para alturas y diametros de {especies[2]}')
  return 0

#%% correr tests desde consola
if __name__ == '__main__':
  print('-- TESTS --')
  test_busquedas()
  print('\n')
  test_inversion()
  print('\n')
  test_propagar()
  print('\n')
  test_arboles()
