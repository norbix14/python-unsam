######################################################################

"""
Contenedores.
"""

"""
2.15
Lista de tuplas.
El archivo `Data/camion.csv` contiene la lista de cajones cargados
en un camión. En el [Ejercicio 2.6] de la sección anterior
escribiste una función `costo_camion(nombre_archivo)` que leía el
archivo y realizaba un cálculo.
Usando este código como guía, creá un nuevo archivo `informe.py`.
En este archivo, definí una función `leer_camion(nombre_archivo)`
que abre un archivo con el contenido de un camión, lo lee y
devuelve la información como una lista de tuplas. Para hacerlo
vas a tener que hacer algunas modificaciones menores al código.
Ver archivo <informe.py>.
"""

"""
2.16
Lista de diccionarios.
Tomá la función que escribiste en el ejercicio anterior y modificala
para representar cada cajón del camión con un diccionario en vez de
una tupla. En este diccionario usá los campos "nombre", "cajones"
y "precio" para representar las diferentes columnas del archivo de
entrada.
Ver archivo <informe.py>.
"""

"""
2.17
Diccionarios como contenedores.
En el [Ejercicio 2.7] escribiste una función que busca el precio de
una determinada fruta o verdura en el archivo `../Data/precios.csv`.
Esto es útil para saber sobre un producto en particular, pero si
necesitás tener los precios de toda la mercadería, no resulta
práctico abrir y cerrar el archivo para consultar cada precio.
Por eso ahora te proponemos generar un diccionario que contenga
todos los precios. En este diccionario, podés consultar luego los
precios de cada producto.
Escribí una función `leer_precios(nombre_archivo)` que a partir
de un conjunto de precios como éste arme un diccionario donde las
claves sean los nombres de frutas y verduras, y los valores sean
los precios por cajón.
Para hacerlo, empezá con un diccionario vacío y andá agregándole
valores igual a como hiciste antes, pero ahora esos valores los
vas leyendo del archivo.
Vamos a usar esta estructura de datos para buscar rápidamente
los precios de las frutas y verduras.
Un par de consejos:
Usá el módulo `csv` igual que antes.
El archivo `Data/precios.csv` puede tener líneas en blanco, esto
te puede traer complicaciones.
(Observá que arriba figura una lista vacía (la última), porque la
última línea del archivo no tenía datos.)
Puede suceder que esto haga que tu programa termine con una
excepción. Usá los comandos `try` y `except` para evitar el
problema.
Para pensar: ¿Sería mejor prevenir estos problemas con el
comando `if` en vez de `try` y `except`?
Una vez que hayas escrito tu función `leer_precios()`, testeala
interactivamente para asegurarte de que funciona bien.
Ver archivo <leer_precios.py>
"""

"""
2.18
Balances.
Supongamos que los precios en `camion.csv` son los precios pagados
al productor de frutas mientras que los precios en `precios.csv`
son los precios de venta en el lugar de descarga del camión.
Ahora vamos calcular el balance del negocio: juntá todo el trabajo
que hiciste recién en tu programa `informe.py`
(usando las funciones `leer_camion()` y `leer_precios()`) y completá
el programa para que con los precios del camión ([Ejercicio 2.16]) y
los de venta en el negocio ([Ejercicio 2.17]) calcule lo que costó
el camión, lo que se recaudó con la venta, y la diferencia.
¿Hubo ganancia o pérdida?
El programa debe imprimir por pantalla un balance con estos datos.
Ver archivo <informe.py>
"""
