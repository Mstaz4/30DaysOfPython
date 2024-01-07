# Day 2: 30 Days of python programming
from math import pow

# Exercises Level 1
first_name = "Luis"
last_name = "Brito"
full_name = "Luis Brito"
country = "Venezuela"
city = "Puerto Ordaz"
age = 22
year = 2024
is_married = False
is_true = True
is_light_on = False

fav_color, dog_name, brother_name = "blue", "Rambo", "Raúl Andrés"

# Exercises level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(fav_color))
print(type(dog_name))
print(type(brother_name))

print("\n", len(first_name))

print("\nWhich name has more lenght?")
if (len(first_name) > len(last_name)):
    print("First name has more lenght")
else:
    print("Last name has more lenght")


num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = pow(num_one, num_two)
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * pow(radius, 2)
circum_of_circle = radius * 2

radius = float(input("Ingresa el radio: "))
area_of_circle = 3.14 * pow(radius, 2)
print("The area is: ", area_of_circle)

first_name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
country = input("Ingrese su país: ")
age = int(input("Ingrese su edad: "))

help('keywords')
