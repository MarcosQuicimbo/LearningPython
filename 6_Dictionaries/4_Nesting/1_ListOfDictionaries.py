# se puede hacer 
# 1. conjunto de diccionario dentro de una lista 
# 2. items de una lista dentro de un diccionario 
# 3. un diccionario dentro de otro diccionario 

alien_0 = {'color': 'gree', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
    
#########
print('\n')
# make empty list for storing aliens 
aliens = []
# make 30 green aliens
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# show the first 5 aliens 
for alien in aliens [0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium-speed'
        alien['points'] = 10
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
for alien in aliens[0:5]:
    print(alien)
print('...')
#show how many aliens have been created
print('total aliens numbers is: ', str(len(aliens)))
    