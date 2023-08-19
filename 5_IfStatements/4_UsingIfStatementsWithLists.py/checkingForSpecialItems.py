# display the message cuando un topping es agregado a la pizza 
# hacer una lista de toppings que el cliente solicita 
# usa un loop para anunciar cada topping mientras es 
# agregado a la pizza 
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('sorry, the ',requested_topping, ' has finished')
    else:
        print(requested_topping)