#make a new list base in the previous one that has already defined 
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]

print("My favorite foods are: ", my_foods)
print("My friend's favorite foods  are: ", friend_food)

#adding elements to my_foods and friend_food
my_foods.append('sancocho')
print(my_foods)
friend_food.append('pastel')
print(friend_food)
my_foods.insert(0, 'papas fritas')
print(my_foods)

## Incorrect way to make a list copy 
my_foods = friend_food

my_foods.append('sopa de fideo')
friend_food.append('menestron')
print(my_foods)
print(friend_food)
