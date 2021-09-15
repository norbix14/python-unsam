#!/usr/bin/env python3
# rebotes.py

######################################################################
"""
@author: Norberto Fabrizio
"""

#%%
# Clase01_1.5

def rebotes(altura):
	"""Mostrar la altura alcanzada de los primeros 10 rebotes.

	Parametros:
		`altura` (int): altura inicial desde donde se arroja.

	Ejemplo:
		>>> rebotes(100)
		'Pelota arrojada desde altura de 100 metros'
		'Rebote Altura'
		1 60.0
		2 36.0
		3 21.6
		4 12.96
		5 7.776
		6 4.6656
		7 2.7994
		8 1.6796
		9 1.0078
		10 0.6047
	"""
	print(f'Pelota arrojada desde altura de {altura} metros')
	print('Rebote Altura')
	alt = int(altura)
	for i in range(1, 11):
		rebote = (alt / 5) * 3
		alt = rebote
		print(i, round(rebote, 4))

#%%
rebotes(100)
