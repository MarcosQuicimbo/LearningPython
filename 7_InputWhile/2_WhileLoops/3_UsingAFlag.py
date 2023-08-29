prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
#message = ""
#while message != 'quit': 
while active:
    message = input(prompt)
    if message == 'quit':
        #print(message)
        active = False
    else: 
        print(message)