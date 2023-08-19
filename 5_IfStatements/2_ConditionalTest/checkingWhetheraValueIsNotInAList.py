# no esta en una lista 
# usar la palabra reservada not in 

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title()+", you can post a response if you wish")
