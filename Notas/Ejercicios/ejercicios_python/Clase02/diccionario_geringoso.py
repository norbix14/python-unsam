#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# diccionario_geringoso.py
"""
@author: Norberto Fabrizio
"""

# 2.14

#%% definicion de la funcion
def diccionario_geringoso(lista = []):
  """Agregar silabas en una palabra luego de una vocal.

  Parametros:
    `lista` (list[str]): lista de palabras a traducir.

  Ejemplo:
    >>> diccionario_geringoso(['banana', 'manzana', 'mandarina'])
    {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}
  """
  vocales = ['a', 'e', 'i', 'o', 'u']
  silabas = ['pa', 'pe', 'pi', 'po', 'pu']
  diccionario = {}
  for palabra in lista:
    geringoso = ''
    for letra in palabra:
      geringoso += letra
      if (letra in vocales):
        geringoso += silabas[vocales.index(letra)]
    diccionario[palabra] = geringoso
  return diccionario

#%%
if __name__ == '__main__':
  print(diccionario_geringoso(['banana', 'manzana', 'mandarina']))
