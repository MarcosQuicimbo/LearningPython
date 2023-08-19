# varios if en bloque, si los if son true, el bloque de codigo 
# de ese if será ejecutado 

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms'in requested_toppings:
    print("Adding ", requested_toppings[0])
if 'peperoni' in requested_toppings:
    print("Adding peperoni", )
if 'extra cheese' in requested_toppings:
    print("Adding ", requested_toppings[1])

print("Finished making your pizza!")