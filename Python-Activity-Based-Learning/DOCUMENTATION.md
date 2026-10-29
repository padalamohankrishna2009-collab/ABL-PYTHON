# Documentation for 10 Python ABL Programs

This document includes the problem statement, objectives, assumptions, algorithm, flowchart representation, pseudocode, code file reference, test cases, and conclusion for each program.

---

## Basic Arithmetic Calculator

**Syllabus mapping:** Unit I — variables, input/output, type conversion, arithmetic operators

### Problem statement
Read two numbers and display their sum, difference, product, quotient, and remainder.

### Objectives
Practice variables, input(), float() conversion, arithmetic operators, and output.

### Assumptions
The second number must not be zero for quotient and remainder.

### Algorithm
1. Start.
2. Read two numbers a and b.
3. Display sum, difference, and product.
4. If b is not zero, display quotient and remainder; otherwise display a message.
5. Stop.

### Flowchart (text representation)
Start → Read a, b → Calculate +, −, × → Check b ≠ 0 → Calculate ÷ and % or show message → Stop

### Pseudocode
```text
INPUT a, b
DISPLAY a + b, a - b, a * b
IF b != 0:
    DISPLAY a / b, a % b
ELSE:
    DISPLAY division unavailable
```

### Python source code
File: `01_basic_arithmetic_calculator.py`

```python
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
```

### Test cases
Input: 10, 3 → Sum 13.0, Difference 7.0, Product 30.0, Remainder 1.0.
Input: 8, 0 → Division-unavailable message.

### Conclusion
Demonstrates input/output, type conversion, arithmetic operators, and an if statement.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.

---

## Student Marks and Grade

**Syllabus mapping:** Unit I and II — arithmetic, input/output, if-elif-else

### Problem statement
Read marks for three subjects, calculate the average, and display a grade.

### Objectives
Use arithmetic expressions and an elif ladder.

### Assumptions
Each mark is from 0 to 100. A: average ≥90; B: ≥75; C: ≥60; D: ≥40; otherwise Fail.

### Algorithm
1. Start.
2. Read three subject marks.
3. Calculate total and average.
4. Choose a grade using if/elif/else.
5. Display total, average, and grade.
6. Stop.

### Flowchart (text representation)
Start → Read marks → Calculate average → Grade decision → Display → Stop

### Pseudocode
```text
INPUT m1, m2, m3
total = m1 + m2 + m3
average = total / 3
IF average >= 90: grade = A
ELIF average >= 75: grade = B
ELIF average >= 60: grade = C
ELIF average >= 40: grade = D
ELSE: grade = Fail
DISPLAY total, average, grade
```

### Python source code
File: `02_student_marks_and_grade.py`

```python
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
```

### Test cases
Input: 95, 90, 94 → Total 279, average 93.0, Grade A.
Input: 45, 50, 55 → Total 150, average 50.0, Grade D.

### Conclusion
Applies arithmetic calculations and an elif ladder to assign a grade.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.

---

## Number Classification

**Syllabus mapping:** Unit II — if/elif/else, relational and arithmetic operators

### Problem statement
Determine whether an integer is positive, negative, or zero and whether it is even or odd.

### Objectives
Practice decision making and modulo operations.

### Assumptions
Input is a valid integer. Zero is even.

### Algorithm
1. Start.
2. Read integer n.
3. Determine positive, negative, or zero.
4. Check n % 2 to determine even or odd.
5. Display both results.
6. Stop.

### Flowchart (text representation)
Start → Read n → Sign decision → Even/odd decision → Display → Stop

### Pseudocode
```text
INPUT n
IF n > 0: DISPLAY positive
ELIF n < 0: DISPLAY negative
ELSE: DISPLAY zero
IF n % 2 == 0: DISPLAY even
ELSE: DISPLAY odd
```

### Python source code
File: `03_number_classification.py`

```python
n = int(input("Enter an integer: "))

if n > 0:
    print("The number is positive.")
elif n < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

### Test cases
Input 7 → positive and odd.
Input -4 → negative and even.
Input 0 → zero and even.

### Conclusion
Demonstrates decision-making statements and relational and arithmetic operators.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.

---

## Multiplication Table

**Syllabus mapping:** Unit II — for loop, range(), string formatting

### Problem statement
Display the multiplication table of a number from 1 through 10.

### Objectives
Use a for loop, range(), arithmetic, and formatted strings.

### Assumptions
The user enters a valid integer.

### Algorithm
1. Start.
2. Read integer n.
3. Repeat i from 1 to 10.
4. Display n × i for each i.
5. Stop.

### Flowchart (text representation)
Start → Input n → Loop from 1 to 10 → Display product → Stop

### Pseudocode
```text
INPUT n
FOR i FROM 1 TO 10:
    DISPLAY n, 'x', i, '=', n * i
```

### Python source code
File: `04_multiplication_table.py`

```python
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

### Test cases
Input 5 → first line 5 x 1 = 5; last line 5 x 10 = 50.
Input 2 → last line 2 x 10 = 20.

### Conclusion
Uses iteration to generate a multiplication table.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.

---

## Star Triangle Pattern

**Syllabus mapping:** Unit II — loops and pattern generation

### Problem statement
Read the number of rows and print a left-aligned triangle of stars.

### Objectives
Understand loop-based pattern generation and string repetition.

### Assumptions
The number of rows must be positive.

### Algorithm
1. Start.
2. Read number of rows.
3. If rows are not positive, display a message.
4. Otherwise print one additional star on each row.
5. Stop.

### Flowchart (text representation)
Start → Input rows → Validate → Print increasing stars → Stop

### Pseudocode
```text
INPUT rows
IF rows <= 0: DISPLAY error
ELSE:
    FOR i FROM 1 TO rows:
        DISPLAY '*' repeated i times
```

### Python source code
File: `05_star_triangle_pattern.py`

```python
rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Please enter a positive number of rows.")
else:
    for i in range(1, rows + 1):
        print("*" * i)
```

### Test cases
Input 4 → *, **, ***, **** on separate lines.
Input 2 → *, ** on separate lines.

### Conclusion
Demonstrates pattern generation using a loop and string repetition.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.

---

## String Analyzer

**Syllabus mapping:** Unit II — strings, string methods, membership operator

### Problem statement
Display the length, uppercase and lowercase forms of text, and check whether it contains 'python'.

### Objectives
Practice len(), upper(), lower(), and the in operator.

### Assumptions
The search is case-insensitive.

### Algorithm
1. Start.
2. Read a sentence.
3. Display its length, uppercase, and lowercase versions.
4. Check whether 'python' appears in the lowercase text.
5. Display the result.
6. Stop.

### Flowchart (text representation)
Start → Input sentence → Apply string methods → Membership check → Display → Stop

### Pseudocode
```text
INPUT text
DISPLAY len(text), text.upper(), text.lower()
IF 'python' in text.lower(): DISPLAY found
ELSE: DISPLAY not found
```

### Python source code
File: `06_string_analyzer.py`

```python
text = input("Enter a sentence: ")

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

if "python" in text.lower():
    print("The sentence contains the word 'python'.")
else:
    print("The sentence does not contain the word 'python'.")
```

### Test cases
Input 'Python is easy' → uppercase PYTHON IS EASY; search found.
Input 'I like coding' → search not found.

### Conclusion
Uses built-in string methods and the membership operator.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.

---

## Palindrome Word Checker

**Syllabus mapping:** Unit II — strings, slicing, if/else

### Problem statement
Check whether a word reads the same forward and backward.

### Objectives
Practice lower(), slicing, and conditional statements.

### Assumptions
The input is a single word; letter case is ignored.

### Algorithm
1. Start.
2. Read a word.
3. Convert it to lowercase.
4. Reverse the word using slicing.
5. Compare original and reversed words.
6. Display result and stop.

### Flowchart (text representation)
Start → Input word → Lowercase → Reverse → Compare → Display → Stop

### Pseudocode
```text
INPUT word
word = lowercase(word)
reverse = word[::-1]
IF word == reverse: DISPLAY palindrome
ELSE: DISPLAY not palindrome
```

### Python source code
File: `07_palindrome_word_checker.py`

```python
word = input("Enter a word: ").lower()
reverse_word = word[::-1]

if word == reverse_word:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
```

### Test cases
Input madam → palindrome.
Input Level → palindrome.
Input hello → not a palindrome.

### Conclusion
Checks string symmetry using slicing and an if-else statement.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.

---

## List Statistics

**Syllabus mapping:** Unit III — lists, append(), list operations

### Problem statement
Read five numbers into a list and display the list, sum, maximum, minimum, and sorted list.

### Objectives
Practice list creation, adding items, and common list operations.

### Assumptions
The user enters five valid numbers.

### Algorithm
1. Start.
2. Create an empty list.
3. Read five numbers and append each.
4. Calculate sum, maximum, and minimum.
5. Display the original and sorted lists.
6. Stop.

### Flowchart (text representation)
Start → Create list → Read and append values → Calculate statistics → Sort → Display → Stop

### Pseudocode
```text
numbers = empty list
REPEAT 5 times:
    INPUT value
    append value to numbers
DISPLAY numbers, sum(numbers), max(numbers), min(numbers)
DISPLAY sorted(numbers)
```

### Python source code
File: `08_list_statistics.py`

```python
numbers = []

for i in range(5):
    value = float(input(f"Enter number {i + 1}: "))
    numbers.append(value)

print("Original list:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sorted list:", sorted(numbers))
```

### Test cases
Inputs 4, 1, 8, 2, 5 → sum 20, max 8, min 1, sorted list [1, 2, 4, 5, 8].

### Conclusion
Demonstrates list creation, append(), and common list operations.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.

---

## Tuple Student Record

**Syllabus mapping:** Unit III — tuples and unpacking

### Problem statement
Store a student's roll number, name, and branch in a tuple, unpack it, and display the details.

### Objectives
Learn tuple creation and unpacking.

### Assumptions
Roll number is an integer; name and branch are strings.

### Algorithm
1. Start.
2. Read roll number, name, and branch.
3. Create a tuple.
4. Unpack the tuple into variables.
5. Display the details.
6. Stop.

### Flowchart (text representation)
Start → Read student details → Create tuple → Unpack → Display → Stop

### Pseudocode
```text
INPUT roll, name, branch
student = (roll, name, branch)
roll_no, student_name, student_branch = student
DISPLAY roll_no, student_name, student_branch
```

### Python source code
File: `09_tuple_student_record.py`

```python
roll = int(input("Enter roll number: "))
name = input("Enter student name: ")
branch = input("Enter branch: ")

student = (roll, name, branch)
roll_no, student_name, student_branch = student

print("Student tuple:", student)
print("Roll number:", roll_no)
print("Name:", student_name)
print("Branch:", student_branch)
```

### Test cases
Input 101, Ravi, CSE → tuple (101, 'Ravi', 'CSE'); fields display correctly.

### Conclusion
Demonstrates tuple creation and unpacking.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.

---

## Set Operations

**Syllabus mapping:** Unit III — sets, set operations, membership testing

### Problem statement
Create two integer sets and display union, intersection, difference, and membership of a value in set A.

### Objectives
Practice set creation, uniqueness, set operations, and membership testing.

### Assumptions
Enter integers separated by spaces. Set display order may vary.

### Algorithm
1. Start.
2. Read two space-separated groups of integers.
3. Convert them to sets.
4. Display union, intersection, and A minus B.
5. Read a number and test membership in A.
6. Display result and stop.

### Flowchart (text representation)
Start → Input groups → Convert to sets → Set operations → Membership check → Display → Stop

### Pseudocode
```text
INPUT line1, line2
A = set of integers in line1
B = set of integers in line2
DISPLAY A | B, A & B, A - B
INPUT x
IF x in A: DISPLAY present
ELSE: DISPLAY absent
```

### Python source code
File: `10_set_operations.py`

```python
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
```

### Test cases
A: 1 2 3; B: 3 4 5; search 2 → union {1,2,3,4,5}, intersection {3}, A-B {1,2}, membership present (order may vary).

### Conclusion
Demonstrates set uniqueness, union, intersection, difference, and membership testing.

**Output screenshot:** Run the program and insert a screenshot of the actual output if your instructor requires one.
