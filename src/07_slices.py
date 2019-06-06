"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
list_slice = slice(1,2)
print(a[list_slice])

# Output the second-to-last element: 9
list_slice = slice(4, 5)
print(a[list_slice])

# Output the last three elements in the array: [7, 9, 6]
list_slice = slice(3, len(a))
print(a[list_slice])

# Output the two middle elements in the array: [1, 7]
list_slice = slice(2, 4)
print(a[list_slice])

# Output every element except the first one: [4, 1, 7, 9, 6]
list_slice = slice(1, len(a))
print(a[list_slice])

# Output every element except the last one: [2, 4, 1, 7, 9]
list_slice = slice(len(a)-1)
print(a[list_slice])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
word_slice = slice(7, 12)
print(s[word_slice])