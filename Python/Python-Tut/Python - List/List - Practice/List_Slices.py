# Lists can be sliced like strings and other sequences.
# Syntax: sliced_list = list_name[startIndex:endIndex]

# This refers to the items of a list starting at index startIndex and stopping just before index endIndex. The default values for list are 0 (startIndex) and the end (endIndex) of the list. If you omit both indices, the slice makes a copy of the original list
color_list = ['Red', 'Blue', 'white', 'Green', 'Black'] # the list has four element: indices start at 0 and end at 3
print(color_list[0:2]) # cut first two items

# Cut second item from a list
color_list1 = ["Red", "Blue", "Green", "Black"] # The list have four element\
print(color_list1[1:2])
print(color_list1[1: -2])

# Cut second and third elements from a list:
color_list2 = ["Red", "Blue", "Green", "Black"] # The list have four element indices start at 0 and end at 3
print(color_list1[1:-1])

# Cut first three items from a list:
color_list3 = ["Red", "Blue", "Green", "Black"] # The list have four element indices start at 0 and end at 3
print(color_list1[:3])

