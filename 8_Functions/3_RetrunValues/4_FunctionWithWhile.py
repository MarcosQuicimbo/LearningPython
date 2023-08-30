def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinitive loop 
continuar = True
while continuar: 
    print("\nPlease enter your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name)
    
    message = input("Deseas ingresar otro nombre (y/n) ")
    if message == 'n': 
        continuar = False