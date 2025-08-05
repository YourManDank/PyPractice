# Consider a game in which the player fights against aliens of differnet colours and point values:
alien_0 = {'colour':'green', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])

# The dictionary alien_0 stores both the variables colour and point value.
# A dictionary is a a collection of key-value pairs, each key is connected to a value and you can use the
# key to access a value associated with the key.

# We wrap a dictionary in braces with a set of key-value pairs inside:
alien_1 = {'colour': 'blue', 'points': 10}
# A key-value pair is simply a set of values that have been associated with one another; and when you provide the key
# python will return the values associated with that key.
# EVERY KEY IS CONNECTED TO IT'S VALUE VIA A COLON : AND INDIVIDUAL KEY-VALUE PAIRS ARE SEPARATED BY COMMAS ,
# You can store as many key-value pairs as you want within an individual dictionary

# In this next dictionary, alien_2, the variable 'colour' is the key and it's value is 'purple':
alien_2 = {'colour': 'purple'}

# In order to retrieve the value associated with the key, we print the name of the dictionary and then place the key inside a set of square brackets:
print(alien_2['colour'])
# This print will return "purple"

# Dictionaries are dynamic and new key-value pairs can be added to them at any time.
# To add a new key-pair value, we give the name of the dictionary followed by the new key in square brackets along with the new value:
# Let's create the dictionary for a pink alien and place it on screen with X and Y co-ordinates:
alien_3 = {'colour': 'pink', 'points': 15}
alien_3['x_position'] = 0
alien_3['y_position'] = 25
print(alien_3)

# A practice dictionary of python terms:
list = {'list' : 'a list allowed us to store sets of items in a list format and we can pull and print individual items from the list using place seleectors'}
variable = {'variable': 'there are four basic types of variable in python: numerical, rating, string and boolean'}
constant = {'constant': 'a constant is a value that doesn ot change throughout a programmes execution'}
statement_or_question = {'= or ==' : ' an = represents a statement; 2=2, a == represents a question; is 2==2?'}
tuples = {'tuples': 'tuples are lists that we place into (parenthesis) rather than [square brackets], python will read the parenthesis and prevent operations from editing the tuple'}
print(list['list'])
print(variable['variable'])
print(constant['constant'])
print(statement_or_question['= or =='])
print(tuples['tuples'])