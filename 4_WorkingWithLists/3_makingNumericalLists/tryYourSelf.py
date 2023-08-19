#counting to twenty 
for value in range(1,21):
    print(value)
    
#make a list of numbers 1 to million 
listNumbers = range(1,1001)
for number in listNumbers:
    print(number)
    
    
#suming a million of numbers 
listNumbers = range(1, 1000001)
min = min(listNumbers)
max = max(listNumbers)
suma = sum(listNumbers)

print(min, max, suma)

#odd numbers 
oddNumbers = list(range (1,20, 2))
for oddNumber in oddNumbers:
    print(oddNumber)
    
# threes 
threeMultiple = list(range(3,30,3))
for threeNumber in threeMultiple:
    print(threeNumber)
    
#cubes 
numbers = list(range(1,11))
for number in numbers:
    cubo = number**3
    print(cubo)
    
#cubes comprehension 
cubes = [number**3 for number in numbers]
print(cubes)