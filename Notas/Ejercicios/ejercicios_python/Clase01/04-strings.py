import re

######################################################################

"""
1.14
Los strings son vectores de caracteres. 
Tratá de extraer algunos carateres.
"""
def extraer_caracteres(frutas):
	print('== Extraer caracteres ==')
	print(frutas[0])
	print(frutas[1])
	print(frutas[2])
	print(frutas[-1])
	print(frutas[-2])

"""
1.15
A pesar de ser sólo de lectura, siempre podés reasignar una variable
a una cadena nueva. Probá el siguiente comando que concatena la
palabra "Pera" al final de `frutas` y "Melón" al principio.
"""
def concatenar_cadena(frutas):
	print('\n== Concatenar cadenas ==')
	frutas = frutas
	frutas = frutas + ',Pera'
	frutas = 'Melón,' + frutas
	print('Melon y Pera agregados')
	print(frutas)

"""
1.16
Experimentá con el operador `in` para buscar subcadenas. 
En el intérprete interactivo probá estas operaciones.
"""
def testeo_pertenencia(frutas):
	a = 'Naranja' in frutas
	b = 'nana' in frutas
	c = 'lima' in frutas
	print('\n== Testeo pertenencia ==')
	print(a)
	print(b)
	print(c)

"""
1.17
Usá el comando `for` para iterar sobre los caracteres de una cadena.
Modificá el código de manera que dentro del ciclo el
programa cuente cuántas letras "o" hay en la cadena.
*Sugerencia: usá un contador como con los meses de la hipoteca.*
"""
def iterar_cadena(cadena):
	contador_o = 0
	print('\n== Iterar cadena ==')
	for i in cadena:
		print(f'Caracter {i}')
		if (i.lower() == 'o'):
			contador_o = contador_o + 1
	print(f'Hay {contador_o} letras o')

"""
1.18
Usá una iteración sobre el string `cadena` para agregar la sílaba
'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
Podés probar tu código cambiando la cadena inicial por otra palabra,
como 'apa' o 'boligoma'.
Guardá el código en un archivo `geringoso.py`.
Ver archivo <geringoso.py>.
"""

"""
1.19
En el intérprete interactivo experimentá con algunos de los métodos
de cadenas introducidos antes.
"""

"""
1.20
Modificá el programa `hipoteca.py` de la sección anterior
para que escriba su salida usando f-strings.
Tratá de hacer que la salida quede bien alineada.
"""

"""
1.21
Una limitación de las operaciones básicas de cadenas es que no
ofrecen ningún tipo de transformación usando patrones más sofisticados.
Para eso vas a tener que usar el módulo `re` de Python y aprender a
usar expresiones regulares. El manejo de estas expresiones es
un tema en sí mismo. A continuación presentamos un corto ejemplo:
"""
def regexp():
	# Encontrar las apariciones de una fecha en el texto
	texto = 'Hoy es 20/7/2021. Mañana será 21/7/2021.'
	fecha = re.findall(r'\d+/\d+/\d+', texto)
	# Reemplazá esas apariciones, cambiando el formato
	fecha_formateada = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto)
	print('\n== RegExp ==')
	print(fecha)
	print(fecha_formateada)

#
frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

#
extraer_caracteres(frutas)
concatenar_cadena(frutas)
testeo_pertenencia(frutas)
iterar_cadena('forloop')
regexp()
