#int function : string -> int 
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You can vote! ")
    
##############################
print("\nRoller coaster")
hight = input("How tall are you, in cm")
hight = int(hight)

if hight >= 180:
    print("You could be a pilot ")
else: 
    print("Sorry, you need to be taller")