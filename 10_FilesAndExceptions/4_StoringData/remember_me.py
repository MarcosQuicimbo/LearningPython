import json

# load the username, if it has been stored previously 
# otherwise, prompt for the username and store it

def get_stored_username():
    """Get stored username if available"""
    file_name = 'C:/Users/Marcos/DataScience/LearningPython/10_FilesAndExceptions/4_StoringData/username.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
    
def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
greet_user()