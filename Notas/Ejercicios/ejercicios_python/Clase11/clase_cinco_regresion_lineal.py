#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clase_cinco_regresion_lineal.py
"""
@author: Norberto Fabrizio
"""

# 11.5 - Regresión lineal

import numpy as np

import matplotlib.pyplot as plt

#%% regresion lineal simple
def reg_lineal_simple():
  x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4])
  y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
  g = plt.scatter(x = x, y = y)
  plt.title('scatterplot de los datos')
  plt.show()

#%% ajuste del modelo de cuadrados minimos
def ajuste_lineal_simple(x, y):
  a = sum(((x - x.mean()) * (y - y.mean()))) / sum(((x - x.mean()) ** 2))
  b = y.mean() - a * x.mean()
  return a, b

#%% ejemplo: datos sinteticos
#
def datos_sinteticos(n = 50, minx = 0, maxx = 500):
  x = np.random.uniform(minx, maxx, n)
  r = np.random.normal(0, 25, n) # residuos simulados
  y = 1.3 * x + r
  g = plt.scatter(x = x, y = y)
  plt.title('gráfico de dispersión de los datos')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()
#
def ajuste_lineal(x, y, minx, maxx):
  a, b = ajuste_lineal_simple(x, y)
  grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
  grilla_y = grilla_x*a + b
  g = plt.scatter(x = x, y = y)
  plt.title('y ajuste lineal')
  plt.plot(grilla_x, grilla_y, c = 'green')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()
#
def ver_ajuste(n = 50, minx = 0, maxx = 500):
  x = np.random.uniform(minx, maxx, n)
  r = np.random.normal(0, 25, n)
  y = 1.3 * x + r
  ajuste_lineal(x, y, minx, maxx)

#%% 11.14 - precio_alquiler ~ superficie
# * ver archivo alquiler.py

#%% ejemplo: relacion cuadratica

#%% parte optativa

#%% regresion lineal multipel

#%% 11.15 - peso especifico

#%% 11.16 - modelo cuadratico

#%% 11.17 - modelos polinomiales para una relacion cuadratica

#%% 11.18 - seleccion de modelos

#%% 11.19 - datos para la evaluacion

#%% 11.20 - altura y diametro de arboles

#%% 11.21 - graficos de ajuste lineal con seaborn
