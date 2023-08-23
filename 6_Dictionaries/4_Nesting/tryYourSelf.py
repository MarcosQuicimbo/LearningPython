print("6.7 People")
mama = {
    'first_name': 'elvia', 
    'last_name': 'cancino',
    'age': 52, 
    'city': 'Minas'
}
papa = {
    'first_name': 'gil', 
    'last_name': 'quichimbo',
    'age': 70, 
    'city': 'Loja'
}
gene = {
    'first_name': 'genesis', 
    'last_name': 'velasquez',
    'age': 23, 
    'city': 'Santo Domingo'
}

people = [mama, papa, gene]
for person in people: 
    print(person)
######################
print("\n 6.8 Pets ")
pet1 = {
    'animal_kind': 'dog',
    'owner_name': 'juan',
}
pet2 = {
    'animal_kind': 'horse',
    'owner_name': 'danilo',
}
pet3 = {
    'animal_kind': 'roster',
    'owner_name': 'maria',
}
pets = [pet1, pet2, pet3]
for pet in pets: 
    for key, value in pet.items():
        print(key,"-->", value)

print("\n 6.9 Favorite places:")
favorite_places = {
    'alice': ['parque', 'playa','montana'],
    'jhon': ['london', 'dubai'],
    'mark': ['cerros']
}

for names, places in favorite_places.items():
    print("For ", names, "Favorite places are:")
    for location in places:
        print("\t",location)
        
print("6.10 Favorite numbers")
favorite_numbers = {
    'marcos': [8,5,1,3], 
    'paulina': [3],
    'jonathan': [2,3], 
    'deisi':  [2],
    'victor': [3,2], 
    'andrea': [21]
}
for names, numbers in favorite_numbers.items():
    print(names, 'favorite numbers are: ')
    for numero in numbers:
        print("\t ", str(numero))

print("\n 6.11 Cities")
cities = {
    'quito': {
        'country': 'ecuador',
        'population': 3000, 
        'export': True,
    } ,
    'santo domingo': {
        'country': 'Dominicana',
        'population': 23000, 
        'export': True,
    } ,
    'bogota':{
        'country': 'colombia',
        'population': 2323200, 
        'export': False,
    } ,
}
for key, value in cities.items():
    print('Ciudad: ', key)
    pais = value['country']
    population = value['population']
    exporta = value['export']
    print('\t ','pais ->', pais, 'population -> ', population, 
          'export -> ', exporta)
    
print('6.12 Extension')
