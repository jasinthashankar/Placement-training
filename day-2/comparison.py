#Comparison
#a = 10
#b = 20
#print(a > b)
#print(a < b)
#print(a == b)
#print(a != b)


a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
if a > b:
    print("A is greater")
elif a < b:
    print("B is smaller")
elif a == b:
    print("Both are equal")
elif a != b:
    print("Both are not equal")
else:
    print("Invalid number")