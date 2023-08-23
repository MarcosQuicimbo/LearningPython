alien = {'color': 'green', 'points':5}
print('The current alien color is ', alien['color'])
alien['color'] = 'yellow'
print('The new alien color is ' ,alien['color'])

print('\n')
alien = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien['x_position']))

#move the alien to the right
#Determine how far to move the alien based on its current speed 
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# The new position is the old position plus the increment 
alien['x_position'] = alien['x_position'] + x_increment
print("New x-position: " + str(alien['x_position']))
