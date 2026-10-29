# Project 01: Basic Arithmetic Calculator
# Syllabus: Unit I — variables, input/output, type conversion, arithmetic operators

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Quotient:", a / b)
    print("Remainder:", a % b)
else:
    print("Quotient and remainder are not defined when the second number is zero.")
