word = input("Enter a word: ").lower()
reverse_word = word[::-1]

if word == reverse_word:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
