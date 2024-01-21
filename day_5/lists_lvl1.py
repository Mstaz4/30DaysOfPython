# 1. Declare an empty list
lista = []

# 2. Declare a list with more than 5 items
lista = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete"]

# 3. Find the length of your list
print(len(lista))

# 4. Get the first item, the middle item and the last item of the list
lista2 = [lista[0], lista[len(lista) // 2], lista[len(lista) - 1]]
print(lista2)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Luis", 22, "1.71 cm", "single", "mz18 casa25"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['facebook', 'google', 'microsoft',
                'apple', 'IBM', 'oracle', 'amazon']

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[::3])

# 10. Print the list after modifying one of the companies
it_companies[0] = 'twitter'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("facebook")

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, "OpenAI")

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())

# 14. Join the it_companies with a string '#;  '

# 15. Check if a certain company exists in the it_companies list.
print('facebook' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
print(it_companies[3:6])

# 21. Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22. Remove the middle IT company or companies from the list
del it_companies[len(it_companies)//2]
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
redux_index = full_stack.index('Redux')
print(redux_index)
full_stack.insert(redux_index+1, 'Python')
full_stack.insert(redux_index+1, 'SQL')
print(full_stack)
