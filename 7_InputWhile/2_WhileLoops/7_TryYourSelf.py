print("7.4 Pizza Toppings ")
prompt = "Enter a toppings: "
while True: 
    message = input(prompt)
    if message == 'quit':
        break
    else: 
        print(message, " has been added")


print("\n 7.5 Movie tickets")
prompt = "Enter your age: "
while True: 
    respond = input(prompt)
    if respond == 'quit':
        break 
    else:
        respond = int(respond)
        if respond < 3:
            print(respond, " years, so, your ticket is free") 
        elif respond < 12:
            print(respond, "years, so, your ticket cost: $10.00")
        else:
            print(respond, "years, so, your ticket cost: $15.00")

