# divide un numero a/b y retorna el resto 
print(4%3)

# if the remainder is 0, so the modulo operator always returns 0.
# You can use this fact to determine if a number is even or odd:

# si el resto de un numero es cero, es par
# si el resto de un numero no es cero, es impart 

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0: 
    print("\n The number, ", number, "is even.")
else: 
    print("\n The number, ", number, "is odd")