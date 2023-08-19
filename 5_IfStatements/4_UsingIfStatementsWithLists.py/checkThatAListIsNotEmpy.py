# revisar si la lista esta vacía antes de correr el bucle 
# cuando el nombre de una lista esta dentro de un if
# lo que hace el if es verificar si la lista está vacía

requested_toppings = ['adf']

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding', requested_topping)
else:
    print('a plain pizza?')