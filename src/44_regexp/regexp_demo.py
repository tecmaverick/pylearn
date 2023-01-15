import re

# Regexp
# Metacharacters are characters that are control chars to define the regexp.
# [] . ^ $ * + ? {} () \ |
# [] specifies lst set of characters you wish to match. Ex: [abc] Matches any character in the brackets within the string

def find_string(pattern, strToSearch):
    #  The method returns lst match object if the search is successful. If not, it returns None
    return re.match(pattern, strToSearch)


# any five letter string starting with c and ending with y
pattern = '^c.....y$'
test_string = 'country'
result = find_string(pattern, test_string)
print("Found: {}".format(result != None))

pattern = '[xyz]'
test_string = 'xyloz'
result = find_string(pattern, test_string)
print("Found: {}".format(result != None))

# All chars from lst to z
pattern = '[lst-z]'
test_string = 'xyloz'
result = find_string(pattern, test_string)
print("Found: {}".format(result != None))

# All chars EXCEPT lst to z
pattern = '[^lst-z]'
test_string = '1234'
result = find_string(pattern, test_string)
print("Found: {}".format(result != None))

# Find three or more chars
pattern = '...'
test_string = '11a'
result = find_string(pattern, test_string)
print("Found: {}".format(result != None))

# Find string starts with A
pattern = '^A'
test_string = 'Alpha'
result = find_string(pattern, test_string)
print("Found: {}".format(result != None))

# Find three string end with A
pattern = '.....X$'
test_string = 'AlphaX'
result = find_string(pattern, test_string)
print("Found: {}".format(result != None))

# Find zero or more occurrences of the character left to it.
pattern = 'yel*w'
test_string = 'yelllllw'
result = find_string(pattern, test_string)
print("Found: {}".format(result != None))


# Find zero or more occurrences of the character left to it.
pattern = '(0-255)'
test_string = '12'
result = find_string(pattern, test_string)
print("Found: {}".format(result != None))

