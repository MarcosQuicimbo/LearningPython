# Removiendo todas instancias de un valor especifico de una lista 
# remove to remove the value of a list 
# remover todas las instancias de un valor 
# usar un while hasta que no haya un 'cat' en la lista de pets

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("Lista original = ", pets)
count = 0
while 'cat' in pets: #mientras haya un valor de 'cat' en la lista pets
    pets.remove('cat')
    count += 1
print("Lista sin 'cat' = ", pets)
print("Cats removed = ", count)