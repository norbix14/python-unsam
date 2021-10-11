#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# clases.py
"""
@author: Norberto Fabrizio
"""

import fileparse

#### 9.2 - Clases

#%% la instruccion class
class Jugador():
  """Clase jugador."""
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y
    self.salud = 100

  def mover(self, dx, dy):
    """Mover al jugador.

    Parametros:
      `dx` (int): distancia en eje x.
      `dy` (int): distancia en eje y.
    """
    self.x += dx
    self.y += dy

  def lastimar(self, pts):
    """Lastimar al jugador.

    Parametros:
      `pts` (int): en cuantos puntos lastimar.
    """
    self.salud -= pts

#### 9.3 - Herencia

#%%
class Lote():
  """Clase Lote para manejar carga de un camion."""
  def __init__(self, nombre, cajones, precio) -> None:
    """Constructor.

    Parametros:
      `nombre` (str): nombre del producto.
      `cajones` (int): cantidad de cajones del producto.
      `precio` (float): precio del cajon del producto.
    """
    self.nombre = nombre
    self.cajones = cajones
    self.precio = precio

  def costo(self):
    """Metodo para calcular el costo del cajon."""
    return self.cajones * self.precio

  def vender(self, cantidad):
    """Metodo para vender cajones.

    Parametros:
      `cantidad` (int): cantidad de cajones a vender.
    """
    self.cajones -= cantidad

#%%
class MiLote(Lote):
  """Clase Lote para manejar carga de un camion."""
  def __init__(self, nombre, cajones, precio, factor) -> None:
    """Constructor.

    Parametros:
      `nombre` (str): nombre del producto.
      `cajones` (int): cantidad de cajones del producto.
      `precio` (float): precio del cajon del producto.
      `factor` (float): factor de incremento.
    """
    super().__init__(nombre, cajones, precio)
    self.factor = factor

  def rematar(self):
    """Metodo para rematar todo el lote."""
    self.vender(self.cajones)

  def costo(self):
    """Metodo para calcular el costo del cajon con un factor de incremento."""
    return self.factor * super().costo()

#### 9.4 - Metodos especiales

#%% metodos especiales para convertir a strings
class Punto():
  """Clase Punto."""
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return f'({self.x}, {self.y})'

  def __repr__(self) -> str:
    return f'Punto({self.x}, {self.y})'

  def __add__(self, b):
    return Punto(self.x + b.x, self.y + b.y)

#### 9.5 - Objetos, pilas y colas

#%% un ejercicio geometrico
# TODO: COMPLETAR
class Rectangulo():
  """Clase Rectangulo."""
  def __init__(self, x, y) -> None:
    self.x = x.x
    self.y = y.y

  def __str__(self) -> str:
    return f'({self.x}, {self.y})'

  def __repr__(self) -> str:
    return f'Rectangulo({self.x}, {self.y})'

  def base(self):
    """Metodo para obtener la medida de la base de un rectangulo."""
    return self.x

  def altura(self):
    """Metodo para obtener la medida de la altura de un rectangulo."""
    return self.y

  def area(self):
    """Metodo para obtener la medida del area de un rectangulo."""
    return self.x * self.y

  def desplazar(self, desplazamiento):
    """Metodo para desplazar el rectangulo en ambas coordenadas."""
    return 0

  def rotar(self):
    """Metodo para rotar el rectangulo sobre su esquina inferior derecha
    en 90 grados a la derecha."""
    return 0

#%% 9.13 - implementar el TAD pila
#
class Pila():
  def __init__(self) -> None:
    """Crear un estado vacio."""
    self.estado = []

  def apilar(self, estado):
    """Apilar el estado en la lista de estados."""
    self.estado.append(estado)

  def desapilar(self):
    """Desapilar el ultimo estado agregado."""
    if (self.esta_vacia()):
      raise ValueError('No hay nada por desapilar.')
    return self.estado.pop()

  def esta_vacia(self):
    """Verificar si el estado esta vacio."""
    return len(self.estado) == 0
#
def mostrar_x_del_estado(estado, el = 'x'):
  """Mostrar el estado de `x` elemento en el `estado`."""
  print(f"Ejecutando {estado['función']}(), x vale {estado['variables'][el]}")

#%% 9.3 - 
def ej_93():
  with open('../Data/camion.csv', 'rt', encoding='UTF-8') as lineas:
    camion_dicts = fileparse.parse_csv(
      lineas,
      select=['nombre', 'cajones', 'precio'],
      types=[str, int, float]
    )
  camion = [
    Lote(d['nombre'], d['cajones'], d['precio'])
    for d in camion_dicts
  ]
  costo_total = sum([c.costo() for c in camion])
  print(costo_total)

#%% un ejercicio geometrico
def ej_geometrico():
  ul = Punto(0, 2)
  lr = Punto(1, 0)
  ll = Punto(0, 0)
  ur = Punto(1, 2)
  r1 = Rectangulo(ul, lr)
  r2 = Rectangulo(ll, ur)
  return r1, r2

#%% 9.13
def ej_913():
  pila = Pila()
  # la ejecución está en la línea 3 de g(). El estado tiene x = 10.
  estado = {
    'función': 'g',
    'próxima_línea_a_ejecutar': 3,
    'variables': {'x': 10, 'b': 45}
  }
  mostrar_x_del_estado(estado)
  # sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
  estado['próxima_línea_a_ejecutar'] = 5
  pila.apilar(estado)
  # llamo a f y ejecuto primeras líneas
  estado = {
    'función': 'f',
    'próxima_línea_a_ejecutar': 3,
    'variables': {'x': 50, 'a': 20}
  }
  mostrar_x_del_estado(estado)
  # termina ejecución de f: se desapila el estado:
  estado = pila.desapilar()
  mostrar_x_del_estado(estado)

#%%
if __name__ == '__main__':
  #
  jugador = Jugador(2, 3)
  #
  un_lote = Lote('Pera', 100, 490.10)
  mi_lote = MiLote('Frutilla', 100, 490.10, 1.25)
  #
  mi_punto = Punto(10, 20)
  mi_otro_punto = Punto(100, 200)
  #
  r1, r2 = ej_geometrico()
  #
  ej_913()
