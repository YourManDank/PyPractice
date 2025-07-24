# Depending on the requirements of the dictionary it can be easier to start with an empty dictionary and then add each
# key-value pair to the dictionary on their own lines:
alien_0 = {}

alien_0['colour'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Enpty dictionaries are typically used to store data supplied by a user with the key keeping being unique to their ID.
# They are also used when code generates large numbers of key-value pairs automatically.

# To modidy the values in a dictionary, give the name of the dictionary with the key in [square brackets] and then add the value:
alien_1 = {'colour': 'blue'}
print(f"The alien is {alien_1['colour']}.")

alien_1 = {'colour': 'green'}
print(f"The alien is {alien_1['colour']}.")
