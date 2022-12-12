# Lists are Mutable
# Items in the list are mutable i.e. after creating a list you can change any item in the list. See the following statements.
color_list = ["Red", "Blue", "Green", "Black"]
print(color_list[0])

color_list[0] = "White" # Change the value of first item "Red" to "White"
print(color_list)
print(color_list[0])

# Convert a list to a tuple in Python
listx = [1, 2, 3, 4]
tuplex = tuple(listx)
print(tuplex)

# How to use the double colon [ : : ]
listx = [x for x in range(10)]
sublist = listx[2:7:2] #list[start:stop:step] #step specify an increment
print(sublist)

sublist=listx[::3] #returns a list with a jump every 2 times.
print(sublist)

sublist = listx[6:2:-2] # when step is negative the jump is made back

print(sublist)

# Find the largest and the smallest item in a list
print(max(listx)) # the max() function of built-in allows know the highest
print(min(listx)) # the min() function of built-in allows to know the lowest

# Compare two lists in Python
listx1, listx2 = [3,5,7,9],[3,5,7,9]
print(listx1 == listx2)
listx1, listx2=[9, 7, 5, 3], [3, 5, 7, 9]	#create two lists equal, but unsorted.
print(listx1 == listx2)

listx1, listx2 =[2, 3, 5, 7], [3, 5, 7, 9]	#create two different list
print(listx1 == listx2)
print(listx1.sort() == listx2.sort())	#order and compare

# Nested lists in Python
listx = [["Hello", "World"], [0, 1, 2, 3, 4, 5]]
print(listx)

print(listx[0][1]) # The first [] indicates the index of outer list.
print(listx[1][3])

listx.append([True, False])  # add new items
print(listx)

listx[1][2]=4
print(listx)

# How can I get the index of an element contained in the list?
listy = list("HELLO WORLD")
print(listy)
index = listy.index("L") # define the index from which you want to search
print(index)

index = listy.index("O", 3, 5) #define the segment of the list to be searched
print(index)

# Using Lists as Stacks
color_list=["Red", "Red", "Green", "Black"]
print(color_list)
color_list.append("White")
color_list.append("Yellow")
print(color_list)
print(color_list.pop())
print(color_list.pop())
print(color_list.pop())
print(color_list)

# Using Lists as Queues

from collections import deque
color_list = deque(["Red", "Blue", "Green", "Black"])
color_list.append("White")  # White arrive
print(color_list)

color_list.append("yellow")  #Yellow arrive
print(color_list)
y = color_list.popleft()
print(y)

# Lowercase in python
s = "ADEgoKE"
print(s.lower())