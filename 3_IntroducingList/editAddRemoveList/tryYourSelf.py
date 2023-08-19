# guest list
print('Guest list')
dinnerNames = ['karen', 'daniela', 'salome']
print('quieres venir a mi fiesta ', dinnerNames[0])
print('quieres venir a mi fiesta ', dinnerNames[1])
print('quieres venir a mi fiesta ', dinnerNames[2])

#changing guest list
print('\n')
print('changing guest list')
print('it seem like ', dinnerNames[2], 'could not be present that day')
print('to solve this little problem we will replace', dinnerNames[2])
dinnerNames[2] = 'genesis'
print('for this one: ', dinnerNames[2])

#print the new list
print('quieres venir a mi fiesta ', dinnerNames[0])
print('quieres venir a mi fiesta ', dinnerNames[1])
print('quieres venir a mi fiesta ', dinnerNames[2])


#more guest 
print('\n')
print('More guest')

dinnerNames.append('juan')
dinnerNames.append('pedro')
dinnerNames.append('maria')
#insert at the beginning 
dinnerNames.insert(0, 'manuela')
dinnerNames.insert(3, 'manolo')
dinnerNames.append('elvia')

print('quieres venir a mi fiesta ', dinnerNames[0])
print('quieres venir a mi fiesta ', dinnerNames[1])
print('quieres venir a mi fiesta ', dinnerNames[2])
print('quieres venir a mi fiesta ', dinnerNames[3])
print('quieres venir a mi fiesta ', dinnerNames[4])
print('quieres venir a mi fiesta ', dinnerNames[5])
print('quieres venir a mi fiesta ', dinnerNames[6])
print('quieres venir a mi fiesta ', dinnerNames[7])
print('quieres venir a mi fiesta ', dinnerNames[8])
#print('quieres venir a mi fiesta ', dinnerNames[9])

#shrinking guest list 
print('\n')
print('shrinking guest list')
print('sorry dears guest, I just have space for two people')
popped_1 = dinnerNames.pop()
print('sorry dear ', popped_1)
popped_2 = dinnerNames.pop()
print('sorry dear ', popped_2)
popped_3 = dinnerNames.pop()
print('sorry dear ', popped_3)
popped_4 = dinnerNames.pop()
print('sorry dear ', popped_4)
popped_5 = dinnerNames.pop()
print('sorry dear ', popped_5)
popped_6 = dinnerNames.pop()
print('sorry dear ', popped_6)
popped_7 = dinnerNames.pop()
print('sorry dear ', popped_7)


print('your are strill in the dinner:',
      dinnerNames[0], ', ', dinnerNames[1])

dinnerNames.remove('karen')
print(dinnerNames)
dinnerNames.remove('manuela')
print(dinnerNames)