first_name = 'YourMan'
last_name = 'Dank'
message = first_name + ' [' + last_name + '] does a programming '
print(message)
# While this type of formatting works, it is hard to anticipate what the outcome of a large string will be without running it, if it is not correctly formatted

first = 'YourMan'
last = 'Dank'
msg = f'{first} [{last}] is a programmer man '
print(msg)
# The "curly" brackets allow us to insert variables into our strings.