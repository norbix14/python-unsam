#!/usr/bin/env python3
# esfera.py

import math

######################################################################
"""
@author: Norberto Fabrizio
"""

#%%
# 1.13

def esfera(radio):
	"""Calcular el volumen de una esfera segun el radio especificado.

	Parametros:
		`radio` (float): radio de la esfera.

	Ejemplo:
		>>> radio = input('Ingresa el radio de la esfera: ')
		'Ingresa el radio de la esfera:' 6
		>>> volumen = esfera(radio)
		>>> print('Volumen de la esfera:', volumen)
		'Volumen de la esfera: 904.7786842338603'
	"""
	volumen = (4 / 3) * math.pi * (float(radio) ** 3)
	return volumen

#%%
radio = 6

#%%
print('Volumen:', esfera(radio))
