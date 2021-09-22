#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clases.py

import sys

import numpy as np

from matplotlib import pyplot as plt

###############################################################################

# 7.7 - La biblioteca matplotlib

#%% 01 - un plot simple
def plot_simple(save = False):
  x = np.linspace(-np.pi, np.pi, 256)
  c, s = np.cos(x), np.sin(x)
  #
  plt.plot(x, c)
  plt.plot(x, s)
  plt.title('plot simple')
  if save:
    plt.savefig('plot_simple.png', dpi=72)
  plt.show()

#%% 02 - un grafico basico
def grafico_basico(save = False):
  x = np.linspace(-np.pi, np.pi, 256)
  c, s = np.cos(x), np.sin(x)
  # Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
  plt.figure(figsize=(8, 6), dpi=80)
  # Crea un nuevo subplot, en una grilla de 1x1
  plt.subplot(1, 1, 1)
  # Plotea el coseno con una línea azul contínua de ancho 1 (en pixeles)
  plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-")
  # Plotea el seno con una línea verde contínua de ancho 1 (en pixeles)
  plt.plot(x, s, color="green", linewidth=1.0, linestyle="-")
  # Rango del eje x
  plt.xlim(-4.0, 4.0)
  # Ponemos marcas (ticks) en el eje x
  plt.xticks(np.linspace(-4, 4, 9))
  # Rango del eje y
  plt.ylim(-1.0, 1.0)
  # Ponemos marcas (ticks) en el eje y
  plt.yticks(np.linspace(-1, 1, 5))
  # titulo
  plt.title('grafico basico')
  # Podemos grabar el gráfico (con 72 dpi)
  if save:
    plt.savefig('grafico_basico.png', dpi=72)
  # Mostramos el resultado en pantalla
  plt.show()

#%% 03 - detalles de un plot simple
def detalles_plot_simple(save = False):
  x = np.linspace(-np.pi, np.pi, 256)
  c, s = np.cos(x), np.sin(x)
  #
  plt.figure(figsize=(10, 6), dpi=80)
  plt.plot(x, c, color="blue", linewidth=2.5, linestyle="-")
  plt.plot(x, s, color="red", linewidth=2.5, linestyle="-")
  plt.xlim(x.min() * 1.1, x.max() * 1.1)
  plt.ylim(c.min() * 1.1, c.max() * 1.1)
  plt.title('detalles plot simple')
  if save:
    plt.savefig('detalles_plot_simple.png', dpi=72)
  plt.show()

#%% 04 - detalles de un plot simple mejorado
def detalles_plot_simple_mejorado(save = False):
  x = np.linspace(-np.pi, np.pi, 256)
  c, s = np.cos(x), np.sin(x)
  #
  plt.figure(figsize=(10, 6), dpi=80)
  plt.plot(x, c, color="blue", linewidth=2.5, linestyle="-", label='coseno')
  plt.plot(x, s, color="red", linewidth=2.5, linestyle="-", label='seno')
  plt.xlim(x.min() * 1.1, x.max() * 1.1)
  plt.ylim(c.min() * 1.1, c.max() * 1.1)
  plt.title('detalles plot simple mejorado')
  plt.legend(loc='upper left')
  # texto de las marcas de los ejes
  plt.xticks(
    [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
    [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$']
  )
  plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])
  # mover contorno
  ax = plt.gca()
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.spines['bottom'].set_position(('data',0))
  ax.yaxis.set_ticks_position('left')
  ax.spines['left'].set_position(('data',0))
  # puntos interesantes
  t = 2 * np.pi / 3
  plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
  plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
  plt.annotate(
    r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
    xy=(t, np.cos(t)), xycoords='data',
    xytext=(-90, -50), textcoords='offset points', fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")
  )
  plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
  plt.scatter([t, ],[np.sin(t), ], 50, color='red')
  plt.annotate(
    r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
    xy=(t, np.sin(t)), xycoords='data',
    xytext=(+10, +30), textcoords='offset points', fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")
  )
  # el diablo esta en los detalles
  for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(
      dict(facecolor='white', edgecolor='None', alpha=0.65)
    )
  # guardar plot
  if save:
    plt.savefig('detalles_plot_simple_mejorado.png', dpi=72)
  # mostrar plot
  plt.show()

#%% main
def main():
  """Funcion principal."""
  args = sys.argv
  if len(args) <= 1:
    print('---- Modo de uso ----')
    print(f'{args[0]} [a] [b]')
    print('----')
    print('Parametro [a]: funcion a llamar.')
    print(f'EJEMPLO: {args[0]} 0')
    print('Parametro [b]: guardar el plot como png.')
    print('[0] no lo guarda, [1] lo guarda')
    print(f'EJEMPLO: {args[0]} 0 0')
  else:
    funciones = [
      plot_simple,
      grafico_basico,
      detalles_plot_simple,
      detalles_plot_simple_mejorado
    ]
    n_func = int(args[1])
    save = False
    if len(args) > 2:
      save = True if int(args[2]) == 1 else False
    try:
      if save:
        print(f'La imagen se ha guardado.')
      funciones[n_func](save)
    except IndexError:
      print(f'No hay funcion en el indice {n_func}.')
      print(f'Hay funciones desde el indice 0 al {len(funciones) - 1}')

#%%
if __name__ == '__main__':
  main()
