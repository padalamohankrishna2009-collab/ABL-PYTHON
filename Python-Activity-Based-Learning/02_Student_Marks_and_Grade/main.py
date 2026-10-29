# Variables, input, arithmetic operators, and if-elif-else

m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))

total = m1 + m2 + m3
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Total marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
