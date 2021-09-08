import random

######################################################################

"""
5
Aleatoriedad.
"""

"""
5.1
Random.
En esta sección veremos algunas de las funciones del módulo `random`.
Este módulo se usa para generar valores pseudo-aleatorios. Desde el
punto de vista práctico, usaremos estos valores como perfectamente
aleatorios (al ser la computadora una máquina determinística sabemos
que esto no es completamente cierto. De hecho, en lo que sigue, por
simplicidad, omitiremos el prefijo pseudo y hablaremos de números
aleatorios aunque no lo sean exactamente).
"""

"""
5.1
Generala servida.
Queremos estimar la probabilidad de obtener una generala servida
(cinco dados iguales) en una tirada de dados. Podemos hacer la
cuenta usando un poco de teoría de probabilidades, o podemos
*simular* que tiramos los dados muchas veces y ver cuántas de esas
veces obtuvimos cinco dados iguales. En este ejercicio vamos a usar
el segundo camino.

Escribí una función `tirar()` que devuelva una lista con cinco
dados generados aleatoriamente. Escribí otra función llamada
`es_generala(tirada)` que devuelve `True` si y sólo si los cinco
dados de la lista `tirada` son iguales.

Luego analizá el siguiente código.
Correlo con `N = 100000` varias veces y observá los valores que
obtenés.
Luego correlo algunas veces con `N = 1000000`
(ojo, hace un millón de experimentos, podría tardar un poco).

¿Por qué varían más los resultados obtenidos con
`N = 100000` que con `N = 1000000`?
¿Cada cuántas tiradas en promedio podrías decir que sale una
generala servida?
¿Cómo se puede calcular la probabilidad de forma exacta?
"""
def tirar():
  tirada = [
    random.randint(1, 6)
    for i in range(5)
  ]
  return tirada

def es_generala(tirada):
  return True if min(tirada) == max(tirada) else False

"""
N = 10000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G / N
print(f'Tire {N} veces. {G} veces saque generala')
print(f'Probabilidad de {prob:.6f} de sacar generala servida')
"""

"""
5.2
Generala no necesariamente servida.
Si uno juega con las reglas originales (se puede volver a tirar
algunos de los cinco dados hasta dos veces, llegando hasta a tres
tiradas en total) siguiendo una estrategia que intente obtener
generala (siempre guardar los dados que más se repiten y tirar
nuevamente los demás) es más probable obtener una generala que si
sólo consideramos la generala servida. 
Escribí un programa que estime la probabilidad de obtener una
generala en las tres tiradas de una mano y guardalo en un archivo
`generala.py`.

Extra:

Hay gente que, si en la primera tirada le salen todos dados
diferentes, los mete al cubilete y tira los cinco nuevamente. 

Otras personas, eligen uno de esos dados diferentes, lo guardan,
y tiran sólo los cuatro restantes.

¿Podés determinar, por medio de simulaciones, si hay una de estas
estrategias que sea mejor que la otra?

Semillas.
A veces queremos generar números (pseudo-)aleatorios de una manera
reproducible. Puede sonar contradictorio, pero no lo es: es aquí
donde se ve claramente la naturaleza pseudo-aleatoria de estos
números. Si fijamos una semilla con el comando 
`random.seed(semilla)`, donde `semilla` es un número entero, la
secuencia de números aleatorios que obtengamos será reproducible
utilizando la misma semilla.
>>> import random
>>> random.seed(31415)
>>> tirada = [random.randint(1,6) for i in range(5)]
>>> print(tirada)
[5, 3, 4, 1, 5]
"""

"""
5.3
Cocumpleaños.
Haciendo miles de experimentos numéricos, estimá la probabilidad de
que en un grupo de 30 personas elegidas al azar, dos cumplan años el
mismo día. Escribí un programita que permita calcular esa
probabilidad asumiendo que el año tiene 365 días.

Modificando un poco tu programa anterior, ¿podés calcular cuántas
personas tiene que haber en un grupo para que sea más probable que
dos cumplan años el mismo día que que todas cumplan en días
diferentes?

Acá quiero mostrar cómo se puede hacer usando el método de Monte 
Carlo para mostrar que con 30 personas en la habitación, las chances
de que haya dos que cumplan años el mismo día supera el 70 por ciento.

Haga lo siguiente:
* numere los días del año del 1 al 365 (suponiendo que no es un año
bisiesto).
Por ejemplo, el número 1 es el 1 de enero y el 365 el 31 de diciembre.

* Dígale al programa que elija 30 números entre esos 365 en forma
aleatoria. Este dato es vital: tienen que ser elegidos al azar.

* Elige un número y lo repone a los 365 que tenía originalmente.
De esta forma, entre los 30 números puede aparecer alguno repetido.

* Cuando haya terminado el proceso y ya tiene estos 30 números fíjese
-justamente- si hay al menos algún par repetido, que corresponderían
al mismo día del año.

* Repita el proceso 10 mil veces (por supuesto, con la ayuda de una
computadora).

* Fíjese en cuántos de los 10 mil casos de muestra aparecen números
repetidos.

* Divida ese número por 10 mil. Verá que el número que obtiene es
(aproximadamente) 0.7129.

¿Cómo se interpreta esto?
Esto significa que con 30 personas en una habitación, las chances de
que haya dos que cumplan años el mismo día ¡supera el 71 por ciento!

Elecciones sin reposicion.
"""
def elecciones_sin_reposicion():
  valores = [1,2,3,4,5,6,7,10,11,12]
  palos = ['oro','copa','espada','basto']
  naipes = [(valor, palo) for valor in valores for palo in palos]
  print(random.sample(naipes, k=3))

"""
5.4
Envido.
Teniendo en cuenta las reglas del Truco
(https://es.wikipedia.org/wiki/Truco_argentino), estimá la
probabilidad de obtener 31, 32 o 33 puntos de envido en una mano.
¿Son iguales estas tres probabilidades? ¿Por qué?

Mezclar.
La última función que queremos introducir es útil en muchos
contextos. En los juegos de naipes, para continuar con nuestro
ejemplo, es muy usual mezclar el mazo entero antes de repartir. En
Python usamos la función `shuffle` del módulo `random`.

Valores continuos.
Además de generar valores (pseudo)aleatorios discretos, también es
posible generar valores continuos. La funcion `random.random()`
genera un número de punto flotante entre 0 y 1.

Ver archivo <envido.py>.
"""

"""
5.5
Calcular PI.
"""

"""
5.6
Gaussiana.

"""
if __name__ == '__main__':
  #
  tirada_rand = tirar()
  print(tirada_rand)
  print('Generala:', es_generala(tirada_rand))
  #
  tirada_eq = [5,5,5,5,5]
  print(tirada_eq)
  print('Generala:', es_generala(tirada_eq))
  #
  elecciones_sin_reposicion()
