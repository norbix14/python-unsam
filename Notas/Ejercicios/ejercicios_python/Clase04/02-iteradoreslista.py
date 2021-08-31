######################################################################

"""
4.2
Listas y busqueda lineal
"""

"""
4.3
Busquedas de un elemento.
Creá el archivo `busqueda_en_listas.py` para guardar tu código de
este ejercicio y el siguiente.
En este primer ejercicio tenés que escribir una función
`buscar_u_elemento()` que reciba una lista y un elemento y devuelva
la posición de la última aparición de ese elemento en la lista
(o -1 si el elemento no pertenece a la lista).

>>> buscar_u_elemento([1,2,3,2,3,4],1)
0
>>> buscar_u_elemento([1,2,3,2,3,4],2)
3
>>> buscar_u_elemento([1,2,3,2,3,4],3)
4
>>> buscar_u_elemento([1,2,3,2,3,4],5)
-1

Agregale al archivo `busqueda_en_listas.py` una función
`buscar_n_elemento()` que reciba una lista y un elemento y devuelva
la cantidad de veces que aparece el elemento en la lista.
Probá también esta función con algunos ejemplos.

Ver archivo <busqueda_en_listas.py>.
"""

"""
4.4
Busqueda de maximo y minimo.
Agregale a tu archivo `busqueda_en_listas.py` una función `maximo()`
que busque el valor máximo de una lista de números positivos.
Python tiene el comando `max` que ya hace esto, pero como práctica
te proponemos que completes el siguiente código:

def maximo(lista):
  '''Devuelve el máximo de una lista, 
  la lista debe ser no vacía y de números positivos.
  '''
  # m guarda el máximo de los elementos a medida que recorro la lista. 
  m = 0 # Lo inicializo en 0
  for e in lista: # Recorro la lista y voy guardando el mayor
      ...
  return m

Probá tu función con estos ejemplos:

>>> maximo([1,2,7,2,3,4])
7
>>> maximo([1,2,3,4])
4
>>> maximo([-5,4])
4
>>> maximo([-5,-4])
0

¿Por qué falla en el último caso?
¿Por qué anda en el caso anterior? 
¿Cómo se puede inicializar m para que la función ande también con
números negativos?
Corregilo y guarda la versión mejorada en el archivo
`busqueda_en_listas.py`.
Si te dan ganas, agregá una función `minimo()` al archivo.

Ver archivo <busqueda_en_listas.py>.
"""

"""
4.5
Invertir una lista.
Escribí una función `invertir_lista(lista)` que dada una lista
devuelva otra que tenga los mismos elementos pero en el orden inverso.
Es decir, el que era el primer elemento de la lista de entrada deberá
ser el último de la lista de salida y análogamente con los demás
elementos.

def invertir_lista(lista):
  invertida = []
  for e in lista: # Recorro la lista
    ... #agrego el elemento e al principio de la lista invertida
  return invertida

Guardá la función en el archivo `invlista.py` y probala con las
siguientes listas:
1. `[1, 2, 3, 4, 5]`
2. `['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']`

Ver archivo <invlista.py>.
"""

"""
4.6
Propagacion.
Imaginate una fila con varios fósforos uno al lado del otro.
Los fósforos pueden estar en tres estados:
nuevos, prendidos fuego o ya gastados (carbonizados).
Representaremos esta situación con una lista *L* con un elemento por
fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido)
o un -1 (carbonizado). 
El fuego se propaga inmediatamente de un fósforo encendido a cualquier
fósforo nuevo que tenga a su lado. Los fósforos carbonizados no se
encienden nuevamente.

Escribí una función llamada `propagar` que reciba un vector con 
0's, 1's y -1's y devuelva un vector en el que los 1's se propagaron a
sus vecinos con 0. Guardalo en un archivo `propaga.py`.
Por ejemplo:

>>> propagar([0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0])
[0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
>>> propagar([0, 0, 0, 1, 0, 0])
[1, 1, 1, 1, 1, 1]

Ver archivo <propaga.py>.
"""
