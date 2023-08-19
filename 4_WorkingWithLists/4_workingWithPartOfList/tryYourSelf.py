#slices 
facultades = ['civil', 'sistemas', 'mecanica',
              'petroleos', 'quimica', 'electrica',
              'icb', 'ambiental', 'agroindustrias']
print("The first three items in the list are: ")
for facultad in facultades[:3]:
    print(facultad)

print('\n')
print("Three items from the middle of the list are: ")
threeItems = facultades[-6:-3]
print(threeItems)

print('\n')
print('The last three items in the list are: ')
lastThreeItems = facultades[-3:]
print(lastThreeItems)


#my pizzas, your pizzas 
print('\n\n')
my_pizzas = ['peperoni', 'margherita', 'hawaiian', 'supreme', 
          'bbq chicken','veggie', 'meat lovers', 
          'buffalo chicken', 'four cheese', 
          'mushroom and olive ']

friend_pizzas = my_pizzas[:]


my_pizzas.append('mozarella')
print('my favorite pizzas flavors are: ')
for my_pizza in my_pizzas:
    print(my_pizza)
print("===============")
print('my friends favorite pizzas are: ')
friend_pizzas.append('vegetaliana')
for friend_pizza in friend_pizzas:
    print(friend_pizza)

#more lopps 
print('\n\n')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)
    
print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)