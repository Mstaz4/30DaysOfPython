from math import pi, pow

""" 
1.- Declare your age as integer variable
2.- Declare your height as a float variable
3.- Declare a variable that store a complex number 
"""
age = 10
height = 65.6
complejo = 4 + 5j

# 4.- Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

print("Calcular el área de un triangulo\n")
base = float(input("Ingresa la base del triángulo: "))
height = float(input("Ingresa la altura del triángulo: "))

area = 0.5 * base * height

print("El area del triangulo es: ", area)

# 5.- Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
print("\nCalcular el perímetro de un triangulo\n")
side_a = float(input("Ingresa el lado a: "))
side_b = float(input("Ingresa el lado b: "))
side_c = float(input("Ingresa el lado c: "))

perimeter = side_a + side_b + side_c
print("El perimetro del triangulo es: ", perimeter)

# 6.- Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print("\nCalcular el área y perímetro de un rectángulo\n")
length = float(input("Ingresa el largo: "))
width = float(input("Ingresa el ancho: "))

area = length * width
perimeter = 2 * (length + width)
print("El área es: ", area)
print("El perimetro es: ", perimeter)


# 7.- Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print("\nCalcular el área y la circunferencia de un círculo\n")
radius = float(input("Ingresa el radio: "))

area = pi * pow(radius, 2)
circumference = 2 * radius * pi

print("El área es: ", area)
print("la circunferencia es: ", circumference)
