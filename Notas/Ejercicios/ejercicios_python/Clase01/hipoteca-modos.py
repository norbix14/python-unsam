#!/usr/bin/env python3
# hipoteca-modos.py

######################################################################
"""
@author: Norberto Fabrizio
"""

#%%
# 1.7

def modo_pago_uno(saldo, tasa, mensual):
	"""Metodo uno, sin adelantos.

	Parametros:
		`saldo` (float): saldo del credito.
		`tasa` (float): tasa de interes.
		`mensual` (float): pago mensual.

	Ejemplo:
		>>> saldo = 500000.0
		>>> tasa = 0.05
		>>> mensual = 2684.11
		>>> modo_pago_uno(saldo, tasa, mensual)
		# debe devolver $966279.6 a 360 meses con 360 pagos
	"""
	total_pagado = 0.0
	meses_pagados = 0
	pagos_realizados = 0
	while saldo > 0:
		saldo = saldo * (1 + tasa / 12) - mensual
		total_pagado += mensual
		meses_pagados += 1
		pagos_realizados += 1
	print('==== Modo de pago 1 ====')
	print('Total pagado: $', round(total_pagado, 2))
	print('Meses pagados:', meses_pagados)
	print('Pagos realizados:', pagos_realizados)

#%%
# 1.8

def modo_pago_dos(saldo, tasa, mensual):
	"""Metodo dos, con adelantos de $1000.- los primeros 12 meses.

	Parametros:
		`saldo` (float): saldo del credito.
		`tasa` (float): tasa de interes.
		`mensual` (float): pago mensual.

	Ejemplo:
		>>> saldo = 500000.0
		>>> tasa = 0.05
		>>> mensual = 2684.11
		>>> modo_pago_dos(saldo, tasa, mensual)
		# debe devolver $929965.62 a 342 meses con 342 pagos
	"""
	adelanto = 1000
	total_pagado = 0.0
	meses_pagados = 0
	pagos_realizados = 0
	while saldo > 0:
		if (meses_pagados < 12):
			pago_mensual_especial = adelanto + mensual
			saldo = saldo * (1 + tasa / 12) - pago_mensual_especial
			total_pagado += pago_mensual_especial
		else:
			saldo = saldo * (1 + tasa / 12) - mensual
			total_pagado += mensual
		meses_pagados += 1
		pagos_realizados += 1
	print('\n')
	print('==== Modo de pago 2 ====')
	print('Total pagado: $', round(total_pagado, 2))
	print('Meses pagados:', meses_pagados)
	print('Pagos realizados:', pagos_realizados)

#%%
# 1.9

def modo_pago_tres(saldo, tasa, mensual):
	"""Metodo tres, con adelantos de $1000.- por 48 meses a partir
	del 6to año de la hipoteca.

	Parametros:
		`saldo` (float): saldo del credito.
		`tasa` (float): tasa de interes.
		`mensual` (float): pago mensual.

	Ejemplo:
		>>> saldo = 500000.0
		>>> tasa = 0.05
		>>> mensual = 2684.11
		>>> modo_pago_tres(saldo, tasa, mensual)
		# debe devolver $880074.1 a 310 meses con 310 pagos
	"""
	pago_extra_mes_comienzo = 61
	pago_extra_mes_fin = 108
	adelanto = 1000
	total_pagado = 0.0
	meses_pagados = 0
	pagos_realizados = 0
	meses_pagados = 0
	meses_adelantados = 0
	while (saldo > 0):
		meses_pagados += 1
		pagos_realizados += 1
		if (meses_pagados >= pago_extra_mes_comienzo and 
				meses_pagados <= pago_extra_mes_fin):
			pago_mensual_especial = adelanto + mensual
			saldo = saldo * (1 + tasa / 12) - pago_mensual_especial
			total_pagado += pago_mensual_especial
			meses_adelantados += 1
		else:
			saldo = saldo * (1 + tasa / 12) - mensual
			total_pagado += mensual
	print('\n')
	print('==== Modo de pago 3 ====')
	print('Total pagado: $', round(total_pagado, 2))
	print('Meses pagados:', meses_pagados)
	print('Pagos realizados:', pagos_realizados)
	print('Meses adelantados:', meses_adelantados)

#%%
saldo = 500000.0
tasa = 0.05
mensual = 2684.11

#%%
modo_pago_uno(saldo, tasa, mensual)
modo_pago_dos(saldo, tasa, mensual)
modo_pago_tres(saldo, tasa, mensual)
