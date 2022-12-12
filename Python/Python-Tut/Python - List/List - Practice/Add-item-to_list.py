# add an item to the end of the list: list.append(x)
color_list=["Red", "Blue", "Green", "Black"]
print(color_list)

color_list.append("Yellow")

print(color_list)

# Insert an item at a given position: list.insert(position, value)
color_list1=["Red", "Blue", "Green", "Black"]
print(color_list1)

color_list1.insert(2, "white") #insert an item at third position
print(color_list1)

# Modify an element by Using the index of the element
color_list2 = ['Red', 'Blue', 'white', 'Green', 'Black']
print(color_list2)

color_list2[2] = "Yellow" #change the third color
print(color_list2)

# Remove an item from the list: list.remove(x) x is item to remove
color_list3 = ['Red', 'Blue', 'white', 'Green', 'Black']
print(color_list3)
color_list3.remove("Black")
print(color_list3)

# Remove all items from the list
color_list4 = ['Red', 'Blue', 'white', 'Green', 'Black']
print(color_list)
color_list4.clear()
print(color_list4)