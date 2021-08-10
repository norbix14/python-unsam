######################################################################

"""
Armar una lista con los nombres de frutas usando `split()`. 
"""
def lista_frutas(frutas):
  f = frutas.split(',')
  print(f)

"""
1.22
Extraccion y reasignacion de elementos.
"""
def extraer(frutas):
  f = frutas.split(',')
  print('\n== Extraer ==')
  print(f)
  print(f[0])
  print(f[1])
  print(f[-1])
  print(f[-2])

def reasignar(frutas):
  f = frutas.split(',')
  print('\n== Reasignar ==')
  f[2] = 'Granada'
  print(f)
  print(f[0:3])
  print(f[-2:])
  compra = []
  compra.append('Pera')
  print(compra)
  f[-2:] = compra
  print(f)

"""
1.23
El ciclo `for` funciona iterando sobre datos en una secuencia. 
Antes vimos que podíamos iterar sobre los caracteres de una cadena
(las cadenas son secuencias). Ahora veremos que podemos iterar
sobre listas también.
"""
def iterar_frutas(frutas):
  f = frutas.split(',')
  print('\n== Iterar sobre frutas ==')
  for i in f:
    print('Fruta:', i)

"""
1.24
Usá los operadores `in` o `not in` para verificar si
'Granada', 'Lima', y 'Limon' pertenecen a la lista de frutas.
"""
def pertenencia(frutas):
  f = frutas.split(',')
  print('\n== Pertenencia ==')
  print(f'Granada IN frutas:', 'Granada' in f)
  print(f'Lima IN frutas:', 'Lima' in f)
  print(f'Limon NOT IN frutas:', 'Limon' not in f)

"""
1.25
Adjuntar, insertar y remover elementos.
* Usar 'append()' para agregar 'Mango' al final de 'frutas'.
* Usar 'insert()' para agregar 'Lima' como segundo elemento.
* Usar 'remove()' para borrar 'Mandarina' de la lista.
* Agregar una segunda copia de 'Banana' al final de la lista.
* Usar 'index()' para ver la primera aparicion de 'Banana'.
* Contar cantidad de apariciones de 'Banana' con 'count()'.
* Borrar primera aparicion de 'Banana'.
"""

"""
1.26
Ordenamiento.
* Usar 'sort()' para ordenar.
* Usar 'sort(reverse=True)' para ordenar al reves.
"""

"""
1.27
Juntar multiples cadenas.
* Usar 'join()' para juntar.
"""

"""
1.28
Listas de cualquier cosa.
"""

"""
1.29
Traductor rustico al lenguaje inclusivo.
Crear archivo <inclusive.py>.
Ver archivo <inclusive.py>.
"""

#
frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'

#
lista_frutas(frutas)
extraer(frutas)
reasignar(frutas)
iterar_frutas(frutas)
pertenencia(frutas)
