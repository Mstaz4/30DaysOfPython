from math import sqrt

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("y = 2x-2")
print("x = 0 | y =", 2*0-2)
print("x = 1 | y =", 2*1-2)
print("x = 2 | y =", 2*2-2)

print("\nCalculo de pendiente")
print("m =", (2-0)/(2-1))
pendiente1 = (2-0)/(2-1)
print("\nIntercepto de X")
print("x = 0 | y = 2(0) - 2 =", 2*0-2)

print("\nIntercepto de Y")
print("y = 0 | x = 2 / 2 = ", 2/2)

# 9. Find the slope and Euclidean distance between point (2, 2) and point (6,10)
print("\n\nCalculo de pendiente y distancia abs")
print("(2, 2) y (6, 10)")
print("m = ", (10 - 2)/(6 - 2))
pendiente2 = (10 - 2)/(6 - 2)

print("\nDistancia euclidiana entre ambos puntos:")
print(sqrt(pow((6 - 2), 2)+pow((10 - 2), 2)))

# 10. Compare the slopes in tasks 8 and 9.
print("\nComparación de pendientes")
if (pendiente1 == pendiente2):
    print("Ambas pendientes son iguales")
elif (pendiente1 < pendiente2):
    print("Pendiente 2 es mayor")
else:
    print("Pendiente 1 es mayor")

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

print("\nValor de y = x^2 + 6x + 9\n")
print("y = (-3)^2 + 6(-3) + 9 =", 12 - 6*3 + 9)
print("y = (-2)^2 + 6(-2) + 9 =", 4 - 6*2 + 9)
print("y = (-1)^2 + 6(-1) + 9 =", 1 - 6 + 9)
print("y = (0)^2 + 6(0) + 9 =", 0 + 0 + 9)
print("y = (1)^2 + 6(1) + 9 =", 1 + 6 + 9)

a = 1
b = 6
c = 9

y1 = (-b + sqrt(pow(b, 2) - 4*a*c)) / 2*a
y2 = (-b - sqrt(pow(b, 2) - 4*a*c)) / 2*a

print("y1 =", y1)
print("y2 =", y2)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
string1 = "python"
string2 = "dragon"

print("\nComparación de sentencias")
print(string1 < string2)

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print("jargon" in "I hope this course is not full of jargon")

# 15. There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

# 16. Find the length of the text python and convert the value to float and convert it to string
print("\nLongitud de sentencia python")
text = str(float(len("python")))
print(text)

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("\nPar o Impar")
if (1 % 2 == 0):
    print("Is even")
else:
    print("Is not even")

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("\nEs igual 7//3 y int(2.7)?")
print(7 // 3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print("'10' y 10: ", type(10) == type('10'))

# 20. Check if int('9.8') is equal to 10
print("int('9.8') y 10: ", type(10) == type(int(9.8)))

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print("\nTrabajación")
# hours = float(input("Enter hours: "))
# pago = int(input("Ingresa pago por hora: "))
# print("Ganacias semanales: ", hours * pago)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live.
print("\nSegundos de vida vividos\n\n")
# years = int(input("Ingresa el número de años que tienes: "))
# print("Has vivido por", years*31536000, "segundos\n")

# 23. Write a Python script that displays the following table
for i in range(1, 6):
    a = i * 1
    b = i * a
    c = i * b
    print(i, "1", a, b, c)
