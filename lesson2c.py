# a dictionary is a data type that stores data in terms of key - value pair
# it is introduced by the use of curly braces {}
# the values stored inside a dictionary can be of any data type


phonebook = {
    "Benson" : "2547890654",
    "mary" : "25478965432",
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# print out benson's number
print(phonebook["Benson"])

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["PSG", "Barcelona", "Argentina"]
    }
# print barcelona - the second team he played for
print(player["teams"][1])
