# key words and & or 
# AND: dos condiciones son verdaderas simultaneamente 
# AND = P ^ Q, p es verdadero y q es verdadero 

age_0 = 22 
age_1 = 18 
rango = age_0 >= 21 and age_1 >= 21 
print(rango)

age_1 = 22 
rango2 = age_0 >= 21 and age_1 >= 21
print(rango2)

# OR = P o Q, p es verdadero o q es verdadero 
age_0 = 19 
age_1 = 22 

rango1 = age_0 > 18 or age_1 < 19
print(rango1)

rango2 = age_0 < 18 or age_1 > 23
print(rango2)