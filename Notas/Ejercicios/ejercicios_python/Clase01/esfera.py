#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# esfera.py
"""
@author: Norberto Fabrizio
"""

import math

#%% 1.13 - 
def esfera(radio):
	"""Calcular el volumen de una esfera segun el radio especificado.

	Parametros:
		`radio` (float): radio de la esfera.

	Ejemplo:
		>>> radio = 6
		>>> print('Volumen de la esfera:', esfera(radio))
		'Volumen de la esfera: 904.7786842338603'
	"""
	volumen = (4 / 3) * math.pi * (float(radio) ** 3)
	return volumen

#%%
if __name__ == '__main__':
	radio = 6
	print('Volumen de la esfera:', esfera(radio))
