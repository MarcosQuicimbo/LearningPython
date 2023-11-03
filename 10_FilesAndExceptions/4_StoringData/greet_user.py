import json

filename = 'C:/Users/Marcos/DataScience/LearningPython/10_FilesAndExceptions/4_StoringData/username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Wellcome back, " + username + "!")