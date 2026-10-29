# String methods, slicing, and if-else

word = input("Enter a word: ")
word = word.lower()
reverse_word = word[::-1]

if word == reverse_word:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
