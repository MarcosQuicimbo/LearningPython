# the if-elif-else statement 
# just one block of code is executed 

# under 4 is free 
# between 4-18 -> $5
# over 18 -> $10

age = 12 
if age < 4: 
    print("Your admission cost $0.")
elif 4<age<18:
    print("Your admission cost is $5. ")
else: 
    print('Your admission cost is $10. ')
    
### version 2 mejorado el codigo 
age = 12 
if age < 4: 
    price = 0
elif 4<age<18:
    price = 5
else: 
    price = 10
print("Your admission cost ", str(price))
