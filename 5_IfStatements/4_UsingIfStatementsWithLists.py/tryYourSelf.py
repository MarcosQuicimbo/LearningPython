print("5.8 hello admin")
#names = ['marcos', 'karen', 'admin', 'freddy']
names = []

for name in names: 
    if name == 'admin':
        print('hola querido ', name)
    else:
        print("hello ", name)
    
print(" \n 5.9 No users")

if names:
    for name in names: 
        if name == 'admin':
            print('hola querido ', name)
        else:
            print("hello ", name)
else:
    print("sin nombres")

print(" \n 5.10 Checking Usernames")
current_users = ['marcos', 'karen', 'gene', 'freddy', 'manuel']
new_users = ['Marcos', 'paola', 'elvia', 'Freddy', 'miguel']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('nombre no disponible', new_user)
    else: 
        print('nombre disponible', new_user)
        
print(" \n 5.11 Ordinal Numbers")
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(number,'st')
    if number == 2:
        print(number,'nd')
    if number == 3:
        print(number,'rd')
    if number > 3:
        print(number,'th')
