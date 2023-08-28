print("7.1 rental car")
brand = input("Enter the brand car you would like to ren: ")
print("That's fine, I will assignee you the last ", brand, "car")

print("7.2 Restaurant seating")
number_of_people = input("Enter how many people are you: -> ")
number_of_people = int(number_of_people)
if number_of_people > 8: 
    print("Sorry, You will have to wait for a bigger table")
else: 
    print("Ok, you table is ready")
    
print("Multiples of ten")
give_me_a_number = input("Enter a number: -> ")
give_me_a_number = int(give_me_a_number)
if give_me_a_number % 10 == 0:
    print(give_me_a_number, "is 10's multiple")
else: 
    print("No es multiple de 10")
