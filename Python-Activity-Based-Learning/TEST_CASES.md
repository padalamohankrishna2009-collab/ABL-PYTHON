# Test Cases — Python Activity-Based Learning

These are suggested manual test cases for the 10 Python activities. Run each program from its project folder using `python main.py`. Actual output formatting can vary slightly; set and floating-point display order may also vary.

## 1. Basic Arithmetic Calculator
| Test | First number | Second number | Expected result |
|---|---:|---:|---|
| 1 | 10 | 2 | Sum 12, difference 8, product 20, quotient 5, remainder 0 |
| 2 | 7 | 3 | Sum 10, difference 4, product 21, quotient 2.333..., remainder 1 |
| 3 | 5 | 0 | Sum 5, difference 5, product 0; division and remainder warning |

## 2. Student Marks and Grade
| Test | Subject marks | Expected result |
|---|---|---|
| 1 | 95, 90, 100 | Total 285, average 95, grade A |
| 2 | 75, 75, 75 | Average 75, grade B |
| 3 | 60, 60, 60 | Average 60, grade C |
| 4 | 40, 40, 40 | Average 40, grade D |
| 5 | 20, 30, 35 | Average below 40, grade Fail |

Assumption: marks are valid numeric values on the institution's expected scale.

## 3. Number Classification
| Test | Input | Expected result |
|---|---:|---|
| 1 | 8 | Positive and even |
| 2 | -3 | Negative and odd |
| 3 | 0 | Zero and even |
| 4 | 11 | Positive and odd |

## 4. Multiplication Table
| Test | Input | Expected result |
|---|---:|---|
| 1 | 5 | Table from 5 x 1 = 5 through 5 x 10 = 50 |
| 2 | 0 | Ten rows with result 0 |
| 3 | -2 | Table from -2 x 1 = -2 through -2 x 10 = -20 |

## 5. Star Triangle Pattern
| Test | Input | Expected result |
|---|---:|---|
| 1 | 1 | One line: `*` |
| 2 | 4 | Lines contain 1, 2, 3, and 4 stars |
| 3 | 0 | Positive-row warning |
| 4 | -2 | Positive-row warning |

## 6. String Analyzer
| Test | Input | Expected result |
|---|---|---|
| 1 | `I like Python` | Correct length; uppercase/lowercase forms; reports word python present |
| 2 | `PYTHON basics` | Reports word python present (case-insensitive) |
| 3 | `Hello world` | Reports word python absent |
| 4 | Empty string | Length 0; empty uppercase/lowercase values; reports word absent |

## 7. Palindrome Word Checker
| Test | Input | Expected result |
|---|---|---|
| 1 | `madam` | Palindrome |
| 2 | `Level` | Palindrome after lowercase conversion |
| 3 | `python` | Not a palindrome |
| 4 | `a` | Palindrome |
| 5 | Empty string | Current implementation treats it as a palindrome |

## 8. List Statistics
Enter five values for each test.
| Test | Inputs | Expected result |
|---|---|---|
| 1 | 1, 2, 3, 4, 5 | Sum 15, max 5, min 1, sorted list ascending |
| 2 | -1, -2, 0, 2, 1 | Sum 0, max 2, min -2, sorted list ascending |
| 3 | 4, 4, 4, 4, 4 | Sum 20, max/min 4 |

## 9. Tuple Student Record
| Test | Roll number | Name | Branch | Expected result |
|---|---:|---|---|---|
| 1 | 101 | Anu | CSE | Tuple and unpacked values display correctly |
| 2 | 0 | Ravi Kumar | ECE | Tuple preserves the entered name and branch |
| 3 | 25 | Meena | IT | All three fields display correctly |

## 10. Set Operations
| Test | Set A input | Set B input | Search in A | Expected result |
|---|---|---|---:|---|
| 1 | `1 2 3` | `3 4 5` | 2 | Union {1,2,3,4,5}; intersection {3}; A-B {1,2}; search present |
| 2 | `1 1 2` | `2 2 3` | 9 | Duplicates removed; union {1,2,3}; intersection {2}; search absent |
| 3 | blank | `7 8` | 7 | A is empty; union {7,8}; intersection and A-B empty; search absent |

Set display order is not guaranteed by Python; compare set membership rather than printed order.

## General validation notes
- Use valid numeric input unless deliberately checking input-error handling.
- The current examples do not all validate malformed input or mark ranges.
- Record the actual output in your lab record and capture your own screenshots of each run.
