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
print(f"The alien is now {alien_1['colour']}.")

# Now lets track the position of an alien that can move at different speeds:
alien_4 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original Position: {alien_4['x_position']}")
# Moving the alien and determining it's speed:
# Using an if-elif-else statement to tell python to test for the speed value and allocate an x increment based on the test result.
if alien_4['speed']== 'slow':
    x_increment = 1
elif alien_4['speed']== 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# New position = Old position + increment
alien_4['x_position'] = alien_4['x_position'] + x_increment
print(f"New Position: {alien_4['x_position']}")

# Removal of key-value pairs using a del statement
alien_2 = {'colour': 'grey', 'points': 5}
print(alien_2)

del alien_2['points']
print(alien_2)
# Deleting a key will also delete it's values.