# We can use the get() method to set a default value that will be returned in the event that a key does not exist; avoiding the error demonstrated later:
# The get() method requires a key as a first argument and we can set a value to be returned if a key does not exist as a second argument:
alien_0 = {'colours' : 'purple', 'speed' : 'medium',}
point_value = alien_0.get('points', 'No point value is assigned')
print(point_value)
# If the keys points value exists in the dictionary then python will return the points value, otherwise it will return the default value "No point value is asssigned".

# Using keys in square brackets in order to retrive a key can result in an error if the key does not exist:
# Asking for the point value of an alien that does not exist:
alien_1 = {'colour' : 'red', 'speed' : 'slow'}
print(alien_1['points'])
# This will yield a "Key Error: 'points'" as the value of the points key is undefined.