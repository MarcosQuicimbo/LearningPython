# all the cars should be printed in title case 
# if the item in the list is 'bmw' should print BMW 

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())