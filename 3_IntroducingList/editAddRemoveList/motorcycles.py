motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Editar elementos en una lista 
print("\n")
print("editar elementos de una lista por indice")
motorcycles[0] = 'totoya'
print(motorcycles)

#agregar elemetos al final de una lista 
print("\n")
print("Agregar elementos al final de una lista")
motorcycles.append('kawasaki')
print(motorcycles)


print("\n")
print("De una lista vacia agregar elementos ")
motos = []
print(motos)
motos.append('honda')
motos.append('yamaha')
motos.append('suzuki')
print(motos)

# Insertar elementos en cualquier posicion 
print("\n")
print("Insertar elementos en una posicion")
motos.insert(0, 'fiat')
print(motos)

# 3 formas para remover elementos 
# 1. por el indice con del 
# 2. por pila con pop() ultimo elemento
# 3. por remove con el valor del indice 
print("\n")
print("Removiendo elemento de una lista con del y su posición")
del motos[2]
print(motos)

#removing with pop()
#elimina el ultimo elemento de una lista 
print('\n')
print("Removiendo elemento con pop() ultimo elemento de la pila ")
nombres = ['marcos', 'juan', 'pedro']
print(nombres)
popped_names = nombres.pop()
print('nombre eliminado de la pila', popped_names)
print('la pila queda:',nombres)

print('\n')
print("Removiendo elemento con pop() cualquier indice")
#pop de cualquier elemento de la lista 
primerNombrePila = nombres.pop(0)
print(primerNombrePila)
print(nombres)

print('\n')
print("Removiendo elemento por el valor del indice ")

# Removiendo por el valor 
print(motos)

motos.remove('honda')
print(motos)