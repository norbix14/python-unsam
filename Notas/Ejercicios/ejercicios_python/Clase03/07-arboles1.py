######################################################################

"""
3.6
Arbolado porteño.
En esta sección haremos algunos ejercicios que integran los
conceptos aprendidos en las clases anteriores. Vamos a manejar
archivos, diccionarios, listas, contadores y el comando `zip`,
entre otras cosas.
Entregá lo que puedas hacer.
Ver archivo <arboles.py>.
"""

"""
3.18
Definí una función `leer_parque(nombre_archivo, parque)` que abra el
archivo indicado y devuelva una **lista de diccionarios** con la
información del parque especificado. La función debe devolver, en una
lista un diccionario con todos los datos por cada árbol del parque
elegido (recordá que cada fila del csv es un árbol).
Sugerencia: basate en la función `leer_camion()` y usá también el
comando `zip` como hiciste en el [Ejercicio 3.9] para combinar el
encabezado del archivo con los datos de cada fila. Inicialmente no te
preocupes por los tipos de datos de cada columna, pero cuando empieces
a operar con una columna modificá esta función para que ese dato sea
del tipo adecuado para operar.
Observación: La columna que indica el nombre del parque en el que se
encuentra el árbol se llama 'espacio_ve' en el archivo CSV.
Probá con el parque "GENERAL PAZ" para tener un ejemplo de trabajo,
debería darte una lista con 690 árboles.
"""

"""
3.19
Escribí una función `especies(lista_arboles)` que tome una lista de
árboles como la generada en el ejercicio anterior y devuelva el
conjunto de especies (la columna 'nombre_com' del archivo) que figuran
en la lista.
Sugerencia: Usá el comando `set` como en la [Sección 2.5].
"""

"""
3.20
Usando contadores como en el [Ejercicio 3.11], escribí una función
`contar_ejemplares(lista_arboles)` que, dada una lista como la que
es generada con `leer_parque()`, devuelva un diccionario en el que
las especies (recordá, es la columna `'nombre_com'` del archivo)
sean las claves y tengan como valores asociados la cantidad de
ejemplares en esa especie en la lista dada.
Luego, combiná esta función con `leer_parque()` y con el método
`most_common()` para informar las cinco especies más frecuentes en
cada uno de los siguientes parques:
- 'GENERAL PAZ'
- 'ANDES, LOS'
- 'CENTENARIO'
"""

"""
3.21
Escribí una función `obtener_alturas(lista_arboles, especie)` que,
dada una lista de árboles como la anterior y una especie de árbol
(un valor de la columna 'nombre_com' del archivo), devuelva una lista
con las alturas (columna 'altura_tot') de los ejemplares de esa
especie en la lista.
Observación: Acá sí, fijate de devolver las alturas como números
(de punto flotante) y no como cadenas de caracteres. Podés hacer esto
modificando `leer_parque`.
Usala para calcular la altura promedio y altura máxima de los
'Jacarandá' en los tres parques mencionados.
Resultados de alturas de 'Jacarandá' en tres parques:
General Paz: max: 16.0 - prom: 10.2
Los Andes: max: 25.0 - prom: 10.54
Centenario: max: 18.0 - prom: 8.96
"""

"""
3.22
Escribí una función `obtener_inclinaciones(lista_arboles, especie)`
que, dada una especie de árbol y una lista de árboles como la
anterior, devuelva una lista con las inclinaciones
(columna 'inclinacio') de los ejemplares de esa especie.
"""

"""
3.23
Combinando la función `especies()` con `obtener_inclinaciones()`
escribí una función `especimen_mas_inclinado(lista_arboles)` que,
dada una lista de árboles devuelva la especie que tiene el ejemplar
más inclinado y su inclinación.
Correlo para los tres parques mencionados anteriormente.
**Resultados.** Deberías obtener, por ejemplo, que en el Parque
Centenario hay un 'Falso Guayabo' inclinado '80' grados.
"""

"""
3.24
Volvé a combinar las funciones anteriores para escribir la función
`especie_promedio_mas_inclinada(lista_arboles)` que, dada una lista
de árboles devuelva la especie que en promedio tiene la mayor
inclinación y el promedio calculado.
**Resultados.** Deberías obtener, por ejemplo, que los 'Álamos
Plateados' del Parque 'Los Andes' tiene un promedio de inclinación
de '25' grados.
"""

"""
Preguntas extras:
¿Qué habría que cambiar para obtener la especie con un ejemplar
más inclinado de toda la ciudad y no solo de un parque?
¿Podrías dar la latitud y longitud de ese ejemplar?
¿Y dónde se encuentra (lat,lon) el ejemplar más alto?
¿De qué especie es?
"""
