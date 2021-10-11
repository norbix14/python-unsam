import random


nombres = ['angel', 'esteban', 'facundo', 'gabriel', 'maria', 'mora', 'romina', 'ruth', 'sofía', 'tomás']
random.shuffle(nombres)


cola_de_espera = []

# llega el primero
cola_de_espera.append(nombres[0])
print(f"Están esperando {cola_de_espera}")

# llega el segundo
cola_de_espera.append(nombres[1])
print(f"Están esperando {cola_de_espera}")

print(f"¿Quién sigue?: {cola_de_espera[0]}")

# llega el tercero
cola_de_espera.append(nombres[2])
print(f"Están esperando {cola_de_espera}")

print(f"¿Quién sigue?: {cola_de_espera[0]}")


atender_a = cola_de_espera.pop(0)
print(f"Pasó {atender_a}")
print("Esperan {cola_de_espera}")

atender_a = cola_de_espera.pop(0)
print(f"Pasó {atender_a}")
print("Esperan {cola_de_espera}")

atender_a = cola_de_espera.pop(0)
print(f"Pasó {atender_a}")
print("Esperan {cola_de_espera}")
