print('6.1 Person')
persona = {
    'first_name': 'elvia', 
    'last_name': 'cancino',
    'age': 12, 
    'city': 'Santo Domingo de los Colorados'
}
print(persona)

print('\n', '6.2 Favorite Numbers')
favorite_numbers = {
    'marcos': 8, 
    'paulina': 7, 
    'jonathan': 5, 
    'deisi': 6, 
    'victor': 19, 
    'andrea': 21    
}
print(favorite_numbers)

print('\n', '6.3 Glossary')
glossary = {
    'print': 'print in the console',
    'and': 'two conditions should be true',
    'if': 'is the conditional word', 
    'else': 'the other option in the if condition', 
    'for': 'the loop to simplify some task'
}
for key, value in glossary.items():
    print(key, '-->', value)
    
    