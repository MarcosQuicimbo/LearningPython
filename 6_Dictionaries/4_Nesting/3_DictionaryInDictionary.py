users = {
    'aeinstein': {
                    'first': 'albert',
                    'last': 'einstein',
                    'location': 'princeton',
                 },
    'mcurie': {
                    'first': 'marie', 
                    'last': 'curie',
                    'location': 'paris', 
              },    
}

for username, user_info in users.items():
    print("Username: ", username, "\n",  
          "full name = ", user_info['first'] + " " + 
                          user_info['last'], "\n",
          "location: ", user_info['location'])