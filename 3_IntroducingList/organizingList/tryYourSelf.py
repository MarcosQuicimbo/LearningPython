#store the cities in a list. 
cities = ['quito', 'pusuqui', 'pintag', 'aloag', 'platas']

#print in the original order 

print("original", cities)

#use sorted(), don't change the original order 
print("ordenada",sorted(cities))

#original order has changed? 
print('original changed', cities)

#sorted() to print 
print('reverse order', sorted(cities, reverse=True))

#original list in order 
print('original order', cities)

#reverse() to change the order of your list
lettersList = ['a', 'm', 'b', 'd', 'e']
print('letras originales', lettersList)
lettersList.reverse()
print('usando reverse', lettersList)
lettersList.reverse()
print('letras originales', lettersList)

lettersList.sort()
print('orderd list with sort',lettersList)

lettersList.sort(reverse=True)
print('orden alfabetico inverso', lettersList)

invitingPeople = ['maria', 'mario', 'pedro', 'juan']
print('numero de personas es: ', len(invitingPeople))

 
