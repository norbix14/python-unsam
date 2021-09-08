#!/usr/bin/env python3
# envido.py

import random

######################################################################
"""
@author: Norberto Fabrizio
"""

# 5.4 - Envido

#%% 5.4 - funcion envido que genera 3 cartas unicas
def envido():
  """Repartir 3 cartas unicas en el truco.

  Ejemplo:
    >>> mano = envido()
    >>> print(mano)
    [(1, 'oro'), (2, 'copa'), (3, 'espada')]
  """
  valores = [1,2,3,4,5,6,7,10,11,12]
  palos = ['oro','copa','espada','basto']
  baraja = [
    (valor, palo)
    for valor in valores
    for palo in palos
  ]
  random.shuffle(baraja)
  mano = random.sample(baraja, k=3)
  return mano

#%% 5.4 - calcular la probabilidad de envido en la primera mano
def prob_envido(n = 100, palo = 'oro', puntos = 31, verbose = False):
  """Estimar la probabilidad de obtener 31, 32, o 33 puntos
  de envido en la primera mano.

  Parametros:
    `n` (int): cantidad de simulaciones.
    `palo` (str): palo con el cual realizar la simulacion.
    `puntos` (int): puntos con los cuales realizar la simulacion.

  Ejemplo:
    >>> from pprint import pprint
    >>> print(prob_envido())
    # comportamiento por defecto
    0.03
    >>> print(prob_envido(n=100, palo='espada', puntos=33))
    0.04
    >>> pprint(prob_envido(verbose=True))
    # comportamiento con simulacion, palo y puntos predefinidos
    {'condicion': 'primera mano',
     'detalles': 'envido de oro de 31 puntos',
     'envido': 3,
     'probabilidad': 0.03,
     'simulaciones': 100}
    >>> pprint(prob_envido(1000, 'copa', 32, verbose=True))
    {'condicion': 'primera mano',
     'detalles': 'envido de copa de 32 puntos',
     'envido': 10,
     'probabilidad': 0.01,
     'simulaciones': 1000}
  """
  n = int(n)
  palo = palo.lower() if type(palo) is str else 'oro'
  puntos = int(puntos)
  plus = 20
  tengo_envido = 0
  condicion = 'primera mano'
  detalles = f'envido de {palo} de {puntos} puntos'
  cabeceras = ('envido','probabilidad','detalles','simulaciones','condicion')
  for _ in range(n):
    puntos_envido = 0
    mano = envido()
    mismo_palo = [
      (valor, naipe)
      for valor, naipe in mano
      if (naipe == palo)
    ]
    puntaje = [
      valor
      for valor, naipe in mismo_palo
      if (valor > 0) and (valor < 10)
    ]
    puntos_envido = sum(puntaje) + plus
    if (puntos_envido >= puntos):
      tengo_envido += 1
  prob = round(tengo_envido / n, 6)
  probabilidad = {
    k: v
    for k, v in zip(
      cabeceras,
      (tengo_envido, prob, detalles, n, condicion)
    )
  } if verbose else prob
  return probabilidad
