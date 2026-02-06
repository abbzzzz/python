# a list is a collection of items ordered in a certain way
# A list is introduced by square brackets
# The items of a list are stored inside of indexes in programming we start counting from index 0
#A list is mutable ie the content of the list can change

cars = ["BMW", "Benze", "Hiance", "Probox", "McLaren", "Prado", "Hyundai"]
print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])

#list slicing- This is creating a list from a given bigger list
print(cars[4:])

# printing from index zero to three
print(cars[:4])

#printing from hiance to probox
print(cars[2:5])

# List mutability
# We use the function append to add an item at the end of a list
cars.append("G-Wagon")
print(cars)

# We use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

# we can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

#we can use the sort function to sort our items in alphabetical order
cars.sort()
print(cars)
