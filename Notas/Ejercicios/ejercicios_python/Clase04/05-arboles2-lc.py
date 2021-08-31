######################################################################

"""
4.5
Arbolado porteño y comprension de listas.
Seguimos con el arbolado porteño. Vamos a realizar ejercicios usando
la tecnica de comprension de listas.

Ver archivo <arboles.py>.
"""

"""
4.15
Lectura de todos los arboles.
Basándote en la función `leer_parque(nombre_archivo, parque)`
del [Ejercicio 3.18], escribí otra `leer_arboles(nombre_archivo)`
que lea el archivo indicado y devuelva una *lista de diccionarios*
con la información de todos los árboles en el archivo. La función debe
devolver una lista conteniendo un diccionario por cada árbol con todos
los datos.
Vamos a llamar `arboleda` a esta lista.
"""

"""
4.16
Lista de altos de Jacarandá.
Usando comprensión de listas y la variable `arboleda` podés por
ejemplo armar la lista de la altura de los árboles.

H=[float(arbol['altura_tot']) for arbol in arboleda]

Usá los filtros (recordar la [Sección 4.3]) para armar la lista de
alturas de los Jacarandás solamente.
"""

"""
4.17
Lista de altos y diametro de Jacarandá.
En el ejercicio anterior usaste una sola linea para seleccionar las
alturas de los Jacarandás en parques porteños. Ahora te proponemos
que armes una nueva lista que tenga pares (tuplas de longitud 2)
conteniendo no solo el alto sino también el diámetro de cada
Jacarandá en la lista.

Esperamos que obtengas una lista similar a esta:

[(5.0, 10.0),
 (5.0, 10.0),
 ...
 (12.0, 25.0),
 ...
 (7.0, 97.0), 
 (8.0, 28.0), 
 (2.0, 30.0), 
 (3.0, 10.0), 
 (17.0, 40.0)]
"""

"""
4.18
Diccionario con medidas.
En este ejercicio vamos a considerar algunas especies de árboles.
Por ejemplo:

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

Te pedimos que armes un diccionario en el que estas `especies` sean
las claves y los valores asociados sean los datos que generaste en
el ejercicio anterior.
Más aún, organizá tu código dentro de una función
`medidas_de_especies(especies,arboleda)` que recibe una lista de
nombres de especies y una lista como la del [Ejercicio 4.15] y
devuelve un diccionario cuyas claves son estas `especies` y sus
valores asociados sean las medidas generadas en el ejercicio anterior.

Vamos a usar esta función la semana próxima.
A modo de control, si llamás a la función con las tres especies del
ejemplo como parámetro 
(['Eucalipto', 'Palo borracho rosado', 'Jacarandá']) y la
`arboleda` entera, deberías recibir un diccionario con tres entradas
(una por especie), cada una con una lista asociada conteniendo
4112, 3150 y 3255 pares de números (altos y diámetros),
respectivamente.

Extra: casi todes usan un `for` para crear este diccionario.
¿Lo podés hacer usando una *comprensión de diccionarios*?
Te recordamos la sintaxis:

diccionario = { clave: valor for clave in claves }

"""
