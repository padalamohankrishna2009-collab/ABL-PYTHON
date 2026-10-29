# Tuples and tuple unpacking

roll = int(input("Enter roll number: "))
name = input("Enter student name: ")
branch = input("Enter branch: ")

student = (roll, name, branch)
roll_number, student_name, student_branch = student

print("Student tuple:", student)
print("Roll number:", roll_number)
print("Name:", student_name)
print("Branch:", student_branch)
