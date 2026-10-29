numbers = []

for i in range(5):
    value = float(input(f"Enter number {i + 1}: "))
    numbers.append(value)

print("Original list:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sorted list:", sorted(numbers))
