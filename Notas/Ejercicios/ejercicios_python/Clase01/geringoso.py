#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# geringoso.py
"""
@author: Norberto Fabrizio
"""

#%% 1.18 - 
def geringoso(cadena):
	"""Agregar una silaba luego de una vocal.

	Parametros:
		`cadena` (str): cadena a traducir.

	Ejemplo:
		>>> geringoso('cadena')
		'capadepenapa'
	"""
	vocales = ['a', 'e', 'i', 'o', 'u']
	silabas = ['pa', 'pe', 'pi', 'po', 'pu']
	traduccion = ''
	for letra in cadena:
		traduccion += letra
		if (letra in vocales):
			traduccion += silabas[vocales.index(letra)]
	return traduccion

#%%
if __name__ == '__main__':
	print(geringoso('cadena'))
