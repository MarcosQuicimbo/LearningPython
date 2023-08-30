# dada una lista de usuarios 
# pasar a lista de no registrados 
# pasar a lista de verificados 
# dejarlos ingresar

# Start with users that need to be verified, 
# and an empty list to hold confirmed users. 

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users. 
# Move each verified user into the list of confirmed users. 

while unconfirmed_users: #recorro la lista de usuarios 
    current_user = unconfirmed_users.pop() #extraer el primero 
    print("Verifying user: ", current_user.title(), "...")
    confirmed_users.append(current_user) # ese usuario extraido agrego a lista de verificados

# Display all confirmed users. 
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
    
    
