# puedes preguntar cuanto como necesites en un loop while 
# se almacena las respuestas y encuestados en un 
# diccionario 

responses = {}
# Set a flag to indicate that polling is active 
polling_active = True

while polling_active: 
    # Prompt for the person's name and response
    name = input("\nWhat is your name: ")
    response = input("\nWhich mountain would you like to climb someday? ")
    
    # Store the response in a dictionary 
    responses[name] = response # name is the key; response is the value 
    
    # Find out if anyone else is goin to take the poll. 
    repeat = input("Would you like to let another person respnod? (y/n)")
    if repeat == 'n': 
        polling_active = False
    
# Polling is complete . Show the results 
print("\n-----Polll Results-------")
for name, respond in responses.items():
    print(name, "would like to climb ", respond)
    
    