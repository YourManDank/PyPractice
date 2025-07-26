# Dictionaries don't just store values about one key, you can use dictionaries to track the values of multiple keys:
favourite_languages = {
    'humphrey': 'python',
    'timmy': 'SQL',
    'eddie': 'C',
    'tom': 'python',
}
# This choice of formatting; staggering the key-vale pairs in their own lines makes the block more legible.
# To look up the favourite language of one of the keys:
language = favourite_languages['timmy'].title()
print(f"Timmy's favourite language is {language}.")