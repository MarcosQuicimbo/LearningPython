# si lo que se desea hacer es recorrer los elementos de una 
# lista se lo puede hacer con un bucle for 

# for cada itemtaken in the list of magicians
# print the name of the itemtaken 

#magician is a temporal variable to loop through the list 
magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(magician.title(), 'that was a great trick!')
    print("I can't wait to see your next trick", magician.title()+'.\n')
print("Thank you, everyone. That was a great magic show!")