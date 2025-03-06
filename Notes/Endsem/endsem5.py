# To find the 5th element of a list
A = [1,2,3,[4,5],6]
print(A[4:5])

# To find the greatest among three number using nestead if
a = 7
b = 5
c = 9
if a > b:
    if c > a:
        print(f"{c} is the greatest")
    else:
        print(f"{a} is the greatest")
else:
    if b > c:
        print(f"{b} is the greatest")
    else:
        print(f"{c} is the greatest")