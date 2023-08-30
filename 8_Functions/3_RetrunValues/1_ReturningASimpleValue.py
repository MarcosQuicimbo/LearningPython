# a function can process the data and then return a value as a result 
# this is the return in a function 
# the return, send the processed value to the function which 
# that made the call. 

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name.title() + " " + last_name.title()
    return full_name

student = get_formatted_name('marcos', 'quichimbo')
print(student)