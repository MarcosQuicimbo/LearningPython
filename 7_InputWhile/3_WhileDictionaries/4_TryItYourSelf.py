print("7.8 Deli ")

sandwich_orders = ['pastrami', 'pernil','pastrami', 'queso', 'pollo','pastrami']
finished_sanduches = []

while sandwich_orders: 
    currently_sanduche = sandwich_orders.pop()
    print("...", currently_sanduche, " is been made")
    finished_sanduches.append(currently_sanduche)
for sanduche in finished_sanduches:
    print(sanduche, "was made")


print("7.9 NO Pastrami ")
print(" Deli has no pastrami more, sorry dears")
while 'pastrami' in finished_sanduches: 
    finished_sanduches.remove('pastrami')
for sanduche_sin_pastrami in finished_sanduches:
    print(sanduche_sin_pastrami)



print("\n 7.10 Dream Vacation")
vacaciones = {}

poll_active = True
while poll_active: 
    user = input("Enter you name: ")
    vacation = input("Where would you like to go on vacations: ")
    
    vacaciones[user] = vacation
    
    respuesta = input("seguimos prguntado (y/n) ")
    if respuesta == 'n':
        poll_active = False
for user, place  in vacaciones.items():
    print(user, " would like to go to ", place)
    