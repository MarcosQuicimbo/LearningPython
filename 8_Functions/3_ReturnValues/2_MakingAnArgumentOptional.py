# make sense to make an optional argument 
def get_formatter_name(first_name, last_name, middle_name = ''):
    if middle_name: # non-empty string as True
        full_name = first_name +' '+ middle_name+ ' '+ last_name
    else: 
        full_name = first_name + ' '+ last_name
    return full_name.title()
nombre = get_formatter_name('marcos', 'quichimbo')
print(nombre)