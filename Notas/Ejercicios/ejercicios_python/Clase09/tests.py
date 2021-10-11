#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tests.py
"""
@author: Norberto Fabrizio
"""

from informe_final import leer_camion

from formato_tabla import crear_formateador, imprimir_tabla

from torre_control import TorreDeControl

#%%
def tablas():
  with open('../Data/camion.csv') as archivo:
    camion = leer_camion(archivo)
    formateador = crear_formateador('txt')
    atributos = ['nombre', 'cajones']
    imprimir_tabla(camion, atributos, formateador)
    print()
    imprimir_tabla(camion, ['nombre', 'cajones', 'precio'], formateador)

#%%
# test
def torre_test():
  torre = TorreDeControl()
  torre.nuevo_arribo('AR156')
  torre.nueva_partida('KLM1267')
  torre.nuevo_arribo('AR32')
  torre.nueva_partida('KB67')
  torre.nueva_partida('DET12')
  torre.nuevo_arribo('AR333')
  torre.ver_estado()
  torre.asignar_pista()
  torre.asignar_pista()
  torre.asignar_pista()
  torre.asignar_pista()
  torre.ver_estado()
  torre.asignar_pista()
  torre.asignar_pista()
  torre.asignar_pista()
  torre.ver_estado()
# ejercicio
def torre():
  torre = TorreDeControl()
  torre.nuevo_arribo('AR156')
  torre.nueva_partida('KLM1267')
  torre.nuevo_arribo('AR32')
  torre.ver_estado()
  torre.asignar_pista()
  torre.asignar_pista()
  torre.asignar_pista()
  torre.asignar_pista()
  torre.ver_estado()

#%%
if __name__ == '__main__':
  #tablas()
  #torre_test()
  torre()
