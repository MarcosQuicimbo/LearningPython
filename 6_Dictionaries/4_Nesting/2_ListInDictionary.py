#store information about a pizza being ordered
pizza = {
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra-cheese'],
}
#summarixe the order
print("Yor ordered a " + pizza['crust'], "-crust pizza" + 
      "with the following toppings:")
for topping in pizza['toppings']:
    print(topping)

########################################
    
print('\n Favorite Language')
favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': [],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_language.items():
    if len(languages) <=1: 
        print(name, "'s favorite language is ", str(languages))
    else:
        print(name.title()+"'s favorite language are: ")
        for language in languages:
            print("\t", language.title())