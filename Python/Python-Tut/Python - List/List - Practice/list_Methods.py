# Remove the item at the given position in the list, and return it
color_list4 = ["Red", "Blue", "Green", "Black"] # The list have four element indices start at 0 and end at 3
print(color_list4)
color_list4.pop(2)
print(color_list4)

# Return the index in the list of the first item whose value is x
color_list5 = ["Red", "Blue", "Green", "Black"]
print(color_list5)
print(color_list5.index("Red"))
print(color_list5.index("Black"))

# Return the number of times 'x' appear in the list
color_list6=["Red", "Blue", "Green", "Black", "Blue"]
print(color_list6.count("Blue"))

# Sort the items of the list in place: list.sort( key=None, reverse=False)[alphabetically ascending]
color_list7=["Red", "Blue", "Green", "Black", "Blue"]
color_list7.sort(key=None, reverse=False)
print(color_list7)
# Reverse the elements of the list in place
color_list8=["Red", "Blue", "Green", "Black", "Blue"]
color_  list8.reverse()
print(color_list8)
# Return a shallow copy of the list
color_list9=["Red", "Blue", "Green", "Black", "Blue"]
color_list9.copy()
print(color_list9)

# Search the Lists and find Element
color_list9=["Red", "Blue", "Green", "Black", "Blue"]
print(color_list9.index("Green"))