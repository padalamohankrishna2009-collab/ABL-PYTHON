# Project 01: Basic Arithmetic Calculator

## Problem Statement
Write a Python program to read two numbers and display their sum, difference, product, quotient, and remainder.

## Objectives
- Use variables and input/output.
- Convert user input to numbers using `float()`.
- Practice arithmetic operators.
- Use an `if` statement to avoid division by zero.

## Algorithm
1. Start.
2. Read two numbers.
3. Display their sum, difference, and product.
4. If the second number is not zero, display quotient and remainder.
5. Otherwise, display a message explaining division is unavailable.
6. Stop.

## Flowchart (text)
Start → Input a and b → Calculate sum, difference, product → Is b nonzero? → Calculate quotient/remainder or show message → Stop

## Pseudocode
```text
INPUT a, b
DISPLAY a + b
DISPLAY a - b
DISPLAY a * b
IF b != 0:
    DISPLAY a / b
    DISPLAY a % b
ELSE:
    DISPLAY division unavailable
```

## Run the program
```bash
python main.py
```

## Test Cases
- Input: 10 and 3 → Sum 13, difference 7, product 30, remainder 1.
- Input: 8 and 0 → Division-unavailable message.

## Conclusion
This program practices variables, input/output, type conversion, arithmetic operators, and a conditional statement.
