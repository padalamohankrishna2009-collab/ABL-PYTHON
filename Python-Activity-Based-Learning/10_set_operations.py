line1 = input("Enter integers for set A, separated by spaces: ")
line2 = input("Enter integers for set B, separated by spaces: ")

A = set(map(int, line1.split()))
B = set(map(int, line2.split()))

print("Set A:", A)
print("Set B:", B)
print("Union:", A | B)
print("Intersection:", A & B)
print("A - B:", A - B)

x = int(input("Enter a number to search in set A: "))
if x in A:
    print(x, "is present in set A.")
else:
    print(x, "is not present in set A.")
