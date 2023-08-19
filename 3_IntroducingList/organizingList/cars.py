#ordenado permanente 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('No order', '\n', cars)

#se imprime ordenado alfabeticamente desde la a en adelante
#cars.sort()
#print('Order alfabeticamente', '\n', cars)

#se imprime contrario al orden alfabetico desde la z en adelante
print('\n')
cars.sort(reverse=True)
print(cars)

#ordenado no permanente 
print('Ordenado no permanente\n')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)

#invertir el orden de una lista
print('\n List in reverse order')
posiciones = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
print(posiciones)
posiciones.reverse()
print(posiciones)

#longitud de una cadena
print(len(posiciones))

