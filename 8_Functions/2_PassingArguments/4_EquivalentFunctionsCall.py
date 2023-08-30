# def describe_pet(pet_name, animal_type='dog'):
# 1 argument is needed 
# positional -> pet_name
# keyword -> pet_name 


def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name='bruno')
describe_pet('perrito')

describe_pet('perrito', 'perro')
describe_pet(pet_name='perrito', animal_type='perro')
describe_pet(animal_type='perro', pet_name='perrito')