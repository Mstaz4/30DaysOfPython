# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print("Thirty " + "Days " + "Of " + "Python")

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print("Coding " + "For " + "All")

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. rint the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
string = "Coding"
print(company.index(string))
print(company.rindex(string))
print(company.find(string))
print(company.rfind(string))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
frase = "Python for Everyone"
print(frase.replace("Everyone", "All"))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
lista_palabras = company.split(" ")
print(lista_palabras)

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
texto = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
lista_palabras = texto.split(", ")
print(lista_palabras)

# 15. What is the character at index 0 in the string Coding For All.
print(company[0])

# 16. What is the last index of the string Coding For All.
print(len(company) - 1)

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
words = frase.split()
acronym = "".join([word[0] for word in words])
print(acronym.upper())

# 19. Create an acronym or an abbreviation for the name 'Coding For All'
words = company.split()
acronym = "".join([word[0] for word in words])
print(acronym.upper())

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rindex("l"))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))

# 24.Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex("because"))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

# 28. Does ''Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# 29. Does 'Coding For All' end with a substring coding?
print(company.endswith("Coding"))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = "   Coding For All      "
string = string.lstrip()
string = string.rstrip()
print(string)

# 31. Which one of the following variables return True when we use the method isidentifier():
print(str.isidentifier("30DaysOfPython"))
print(str.isidentifier("thirty_days_of_python"))

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
libraries = " ".join(libraries_list)
print(libraries)

# 33. Use the new line escape sequence to separate the following sentences.
print("""
      I am enjoying this challenge.\n
      I just wonder what is next.\n
      """
      )

# 34. Use a tab escape sequence to write the following lines.
print("""
Name\t\tAge\tCountry\tCity
Asabeneh\t250\tFinland\tHelsinki
      """
      )
# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area or a circle with radius {radius} is {area:.0f} meters square")

# 36. Make the following using string formatting methods:
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
