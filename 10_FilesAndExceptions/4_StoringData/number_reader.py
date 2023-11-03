import json

file_name = 'C:/Users/Marcos/DataScience/LearningPython/10_FilesAndExceptions/4_StoringData/numbers.json'
with open(file_name) as f_obj:
    numbers = json.load(f_obj)
    
print(numbers)
