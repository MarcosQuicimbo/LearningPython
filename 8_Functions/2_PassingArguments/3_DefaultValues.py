# puedes definir un valor por defecto para cada parametro 
# el valor del argumento en la llamada tiene mayor precedencia 
# que el valor por defecto 

# si te das cuenta que la mayoria de los animales son 'dog'
# set the default animal_type = 'dog'

def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
#describe_pet(pet_name='bruno')
describe_pet()
