import sys
import math

print("1. Check the python version you are using\n")
print("\tPython version: ", sys.version)

print('\n2. Operations')
a = int(3)
b = int(4)

print("\tadition. 3 + 4 =", a + b)
print("\tsubtraction. 3 - 4 =", a - b)
print("\tmultiplication. 3 * 4 =", a * b)
print("\tmodulus. 3 % 4 =", a % b)
print("\tdivision. 3 / 4 =", a / b)
print("\texponential. 3 ** 4 =", a ** b)
print("\tfloor division. 3 // 4 =", a // b)

print('\n3. Strings')
print("\tMy name is Luis Daniel")
print("\tMy family name is Brito Caraballo")
print("\tMy country is Venezuela")
print("\tI am enjoying 30 days of python")

print('\n3. Check the data type of the following data')
print("\t10 is", type(10))
print("\t9.8 is", type(9.8))
print("\t3.14 is", type(3.14))
print("\t4 - 4j is", type(4 - 4j))
print("\t ['Asabeneh', 'Python', 'Finland'] is",
      type(['Asabeneh', 'Python', 'Finland']))
print("\tLuis Daniel is", type('Luis Daniel'))
print("\tBrito Caraballo is", type('Brito Caraballo'))
print("\tVenezuela is", type('Venezuela'))

print('\n4. Examples from differents Python Data Types')
# Numbers
integer = int(4)
float = float(45.8)
complex = complex(8 + 5j)

# String
sentence = 'abcdario'

# Boolean
a = True

# List
lista = [1, 4, 8, 7]

# Dictionary
Diccionario = {"maria": "juana"}

# Tuple
Tupla = (1, 2, 3, 4)

# Set
Set = {1, 2, 3, 4, 5}

print('\n5. Find an Euclidian distance between (2, 3) and (10, 8)')

Xaxis = (2, 3)
Yaxis = (10, 8)
x = pow((Xaxis[0]-Yaxis[0]), 2)
y = pow((Xaxis[1]-Yaxis[1]), 2)
answer = math.sqrt(x + y)

print(answer)
