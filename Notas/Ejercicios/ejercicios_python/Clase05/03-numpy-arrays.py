######################################################################

"""
# 5.3 - NumPy
"""

"""
Instalar e importar numpy.

conda install numpy
pip install numpy
pip3 install numpy

import numpy as np
"""

"""
Diferencia entre listas y arreglos.
"""

"""
Arreglos n-dimensionales.
"""

"""
Mas informacion sobre arreglos.
"""

"""
Crear un arreglo basico.

import numpy as np

np.array([1,2,3,4])
np.zeros(2)
np.ones(2)
np.empty(2)
np.arange(4)
np.arange(1,10,2)
np.linspace(0,10,num=5)
"""

"""
Ejercicios.
"""

"""
5.7 - arange() y linspace().
# Especificar el tipo de dato.

por defecto es flotante
np.ones(2, dtype=np.float64)

x = np.ones(2, dtype=np.int64)

# Agregar, borrar y ordenar elementos.

arr = np.array([2,5,3,4,6,1,7,8])
np.sort(arr)
array([1,2,3,4,5,6,7,8])

arr2 = np.array([9,10,11,12])
np.concatenate((arr, arr2))
array([1,2,3,4,5,6,7,8,9,10,11,12])

x = np.array([1,2], [3,4])
y = np.array([5,6])
np.concatenate((x,y), axis=0)
array([[1,2],
  [3,4],
  [5,6]])

# Conocer el tamaño, dimesiones y forma de un arreglo.
`ndarray.ndim` dice la cantidad de ejes o dimensiones.
`ndarray.shape` dara una tupla de enteros indicando cantidad
de elementos en cada eje.
`ndarray.size` dice la cantidad de elementos del arreglo. es el
producto de la tupla `shape`.

# Cambiar la forma de un arreglo.
`arr.reshape()` da nueva forma al arreglo sin cambiar los datos.
tener en cuenta que se debe tener la misma cantidad de elementos.

# Agregar un nuevo eje a un arreglo.
`np.newaxis`.

# Indices y rebanadas.
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a[a[a < 5]]              -> [1,2,3,4]
a[a[a >= 5]]             -> [5,6,7,8,9,10,11,12]
a[a[a%2==0]]             -> [2,4,6,8,10,12]
a[a[(a > 2) & (a < 11)]] -> [3,4,5,6,7,8,9,10]
a[a[(a > 5) | (a == 5)]] -> [[False False False False]
                             [True True True True]
                             [True True True True]]
b = np.nonzero(a < 5)
b -> (array([0,0,0,0]), array([0,1,2,3]))

# Crear arreglos usando datos existentes.
metodo `copy()`.
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

b = a[0, :]        -> array([1,2,3,4])
b[0] = 10          -> array([10,2,3,4])
a[0]               -> array([10,2,3,4]) 

c = a[0, :].copy() -> array([10,2,3,4])
c[1] = 20          -> array([10,20,3,4])
a[0]               -> array([10,2,3,4])

# Operaciones basicas sobre arreglos.


# Broadcasting.
data = np.array([1.0, 2.0])
data * 1.6 -> array([1.6, 3.2])

# Operaciones un poco mas complejas.
`min`, `max`, `sum`, `mean`, `prod`, `std`, etc.

# Crear matrices.


# Formulas matematicas.


# Guardar y cargar objetos de numpy.


"""

"""
5.8 - Guardar temperaturas.

Ampliá el código de la función `medir_temp(n)` en tu archivo 
`termometro.py` que escribiste en el [Ejercicio 5.6] para que
además de devolver las temperaturas simuladas, guarde el vector
con estas temperaturas en el directorio `Data` de tu carpeta de
ejercicios, en un archivo llamado `temperaturas.npy`.
Hacé que corra `n = 999` veces. 

Este ejercicio te lo vamos a pedir en el cierre de clase.
"""

"""
5.9 - Empezando a plotear.

En un rato vamos a empezar a hacer gráficos con Python.
Aquí solo un botón de muestra.

Escribí una función `plotear_temperaturas()` en un archivo
`plotear_temperaturas.py` que lea el archivo de datos
`temperaturas.npy` (debería tener las 999 mediciones simuladas
que creaste recién) y haga un histograma de las temperaturas
simuladas. Te podés basar en el siguiente ejemplo:

import matplotlib.pyplot as plt
plt.hist(temperaturas,bins=25)
plt.show()

# el show no hace falta en algunos entornos.
# A veces lo omitiremos.

Ajustá la cantidad de `bins` para que el gráfico se vea lo
mejor posible.
"""
