import csv 
from matplotlib import pyplot as plt 
from datetime import datetime

filename = 'C:/Users/Marcos/DataScience/LearningPython/16_Downloading_Data/sitka_weather_07-2014.csv'

#Get hig temperatures from file.  
with open(filename) as f: 
    reader = csv.reader(f)
    header_row = next(reader)
    # returns the next line in the file when passed the reader object
    # print(header_row)
    
    # Printing the headers and their positions
    
# for index, column_header in enumerate(header_row):
#    print(index, column_header)

    dates, highs = [], [] # empty list 
    for row in reader: # itera sobre todas las filas del file
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high) # el bucle inicia en la siguiente linea 
                             # como el next(reader) ya leyó el primer registro
                             # continua desde el segundo registro

# Plotting data in a temperature chart 

fig = plt.figure(figsize=(10,6))
plt.plot(dates, highs, c= 'red')

# Format plot
plt.title('Daily high temperatures, July 2014', fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
    


