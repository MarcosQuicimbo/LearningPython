#genera números de uno en uno 
numbers = list(range(1,6))
print(numbers)

#genera numeros en salto de 2 
numbers = list(range(1,6,2))
print(numbers)

#lleno una lista con valores generados en un bucle 
lista = []
for value in range(1,6): 
    #cuadrado = value**2
    lista.append(value**2)
print(lista)