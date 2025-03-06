# Define a list a.
listA = [57, 8, 69, 15, 30]
# Define a list b.
listB = ['Ram', 10, 'bull', 15]

# Find the length of listA & listB.
print(len(listA))
# Sort List A in  ascending order and find the highest element inside it.
sorted_num = sorted(listA)
highest = max(sorted_num)
print(highest)
# Make a new list consisiting of first 3 elements from list A using slice method.
newlist = listA[:3]
print(newlist)
# Add elements of list B to List A.
listA.extend(listB)
print(listA)