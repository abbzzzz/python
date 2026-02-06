# A turple is an immutable type of a list (it cannot change)
# To introduce a turple we use parenthesis()

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")
print(counties)
print(type(counties))

# slicing tuples
print(counties[3:])

# accessing items of a tuple
print(counties[5])

# below will generate an error
counties.append("Machakos")
print(counties)