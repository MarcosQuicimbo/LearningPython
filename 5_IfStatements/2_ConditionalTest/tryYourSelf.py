# conditional test 
car = 'subaru'
print("Is car == 'subaru'? I preducted true")
print(car == 'subaru')

print("/n Is car == 'audi'? I predicted False")
print(car == 'audi')

print('\n')

test1 = 8 < 19
test2 = 21 > 23
test3 = 1>= 2
test4 = 3<= 1
test5 = 'toyota'

tests = [8 < 19, 21 > 23, 1>= 2]
for test in tests: 
    print(test)

print('\n')

test_equaly = "marcos"
print(test_equaly == 'Marcos')

print(1>= 2)

marca_Carro = 'Mazerati'
print(marca_Carro.lower()=='mazerati')

print('\n')
day = 'saturday'
numberOfDay = 6
if day == 'saturday' and numberOfDay == 6:
    print('hoy es sabado 6')
else:
    print('no')

if day == 'saturday' or numberOfDay == 5:
    print('hoy es sabado 6')
else:
    print('no')

print('\n')
brandComputersList = ['toshiba', 'samsum', 'dell', 'hp', 'acer']
laptop = 'apple'
if laptop in brandComputersList:
    print('we have this laptop')
else:
    print('sorry')

fruitsList = ['apple', 'pear', 'lemon', 'melon', 'peneapple']
fruit = 'pear'
if fruit not in fruitsList:
    print('we will get this soon')
else:
    print('there you go')