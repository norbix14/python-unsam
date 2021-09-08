#!/usr/bin/env python3
# tests.py

import random
from pprint import pprint

import generala
import envido
import estimar_pi
import termometro
import plotear_temperaturas as plotear
import figuritas
import arboles

######################################################################

#%% test generala
def test_generala():
  g = generala
  tirada_fija = [5,1,3,5,5]
  print('jugada fija de pruebas:', tirada_fija)
  print('es generala:', g.es_generala(tirada_fija))
  #
  tirada_rand = g.tirar()
  print('jugada aleatoria:', tirada_rand)
  print('es generala:', g.es_generala(tirada_rand))
  #
  N = 10000
  G = sum([g.es_generala(g.tirar()) for _ in range(N)])
  prob = g.probabilidad(G, N)
  print(f'Tire {N} veces. {G} veces saque generala')
  print(f'Probabilidad de {prob} de sacar generala servida')

#%% test probabilidad generala
def test_prob_generala():
  g = generala
  n = 10000
  prob = g.prob_generala(n)
  print('Probabilidad de tener generala servida')
  print('en una mano de 3 tiradas')
  print(f'con {n} simulaciones')
  print(f'Probabilidad del {prob}')

#%% test de probabilidad
def test_probabilidad():
  g = generala
  N = 10000
  G = sum([g.es_generala(g.tirar()) for _ in range(N)])
  prob = g.probabilidad(G, N)
  print('probabilidad:', prob)

#%% test de envido
def test_prob_envido(n = 10):
  e = envido
  #
  print('--errores--')
  pprint(e.prob_envido('100', 100, '100'))
  #
  print('--correctos--')
  N = 1000
  palos = ['basto','copa','espada','oro']
  puntos = [31,32,33]
  for _ in range(n):
    palo = palos[random.randint(0,3)]
    punto = puntos[random.randint(0,2)]
    pprint(e.prob_envido(N, palo, punto))

#%% test de estimar PI
def test_estimar_pi():
  e = estimar_pi
  print(e.generar_punto())
  print(e.gaussiana())

#%% test de medir_temp de termometro
def test_termometro_medir_temp():
  t = termometro
  pprint(t.medir_temp())

#%% test de resumen_temp de termometro
def test_termometro_resumen_temp():
  t = termometro
  print(t.resumen_temp())

#%% test de ploteo
def test_ploteo():
  p = plotear
  p.plotear_temperaturas()

#%%
def main():
  print('ARCHIVO DE PRUEBAS')
  print()
  return None

#%%
if __name__ == '__main__':
  main()
  #
  #test_generala()
  #
  #test_prob_generala()
  #
  #test_probabilidad()
  #
  #test_prob_envido()
  #
  #test_estimar_pi()
  #
  #test_termometro_medir_temp()
  #
  #test_termometro_resumen_temp
  #
  #test_ploteo()
