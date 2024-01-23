# Level 1
# 1. Create an empty tuple
tupla = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('raul', 'andres')

sisters = ('daniela', 'luisanglys')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = siblings + ('raul', 'solima')
print(family_members)

# Level 2
# 6. Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print(siblings)
print(f"{father} and {mother}")

# 7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'pineapple', 'avocado', 'strawberry')
vegetables = ('carrot', 'onion', 'potato')
animal_product = ('meat', 'milk', 'egg')

food_stuff_tp = fruits + vegetables + animal_product

# 8. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 9. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(
    f"{food_stuff_lt[len(food_stuff_lt)//2-1]}  y {food_stuff_lt[len(food_stuff_lt)//2]} ")

# 10. Slice out the first three items and the last three items from food_staff_lt list
print(f"{food_stuff_lt[0:3]}  y {food_stuff_lt[-3:]} ")

# 11. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 12. Check if an item exists in tuple:
#   - Check if 'Estonia' is a nordic country
#   - Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
