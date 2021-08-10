######################################################################
# ejercicios con fstrings

def f_strings():
	nombre = 'Naranja'
	cajones = 100
	precio = 91.1
	a = f'{nombre:10s} {cajones:10d} {precio:10.2f}'
	b = f'Costo = ${cajones * precio:0.2f}'
	print(a)
	print(b)

#
f_strings()
