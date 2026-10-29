rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Please enter a positive number of rows.")
else:
    for i in range(1, rows + 1):
        print("*" * i)
