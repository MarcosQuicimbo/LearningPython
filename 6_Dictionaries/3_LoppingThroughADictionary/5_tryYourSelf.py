print("6.4 Glossary 2. ")
glossary = {
    'print': 'print in the console',
    'and': 'two conditions should be true',
    'if': 'is the conditional word', 
    'else': 'the other option in the if condition', 
    'for': 'the loop to simplify some task', 
    'range': 'allow to set a range of values', 
    'comillas': 'allow to work with text in print', 
    'sort': 'give the function to sort',
    'remove': 'give the availability to remove an item', 
    'item': 'return the key and value in the dictionary'
}
for key, value in glossary.items():
    print(key, '-->', value)

print('\n 6.5 Rivers') 
rivers = {
    'egypt': 'nile', 
    'ecuador': 'guayas', 
    'colombia': 'caqueta', 
    'argentina': 'rio de la plata',
    'peru': 'amazonas'
}
for key, value in rivers.items():
    print('The ', value, 'run in ', key)
    
for value in rivers.values():
    print(value)
    
for key in rivers.keys():
    print(key)
    


print('\n6.6 Polling')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


no_fill_poll_yet = ['marcos', 'martina', 'julie', 'sarah', 'phil']
for name in no_fill_poll_yet:
    if name in favorite_languages.keys():
        print('ya llenaste la encuesta', name)
    else:
        print('llena la encuesta', name)