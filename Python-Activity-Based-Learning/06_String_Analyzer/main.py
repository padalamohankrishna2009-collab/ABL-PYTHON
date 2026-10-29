# String length, string methods, and membership operator

sentence = input("Enter a sentence: ")

print("Length:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

if "python" in sentence.lower():
    print("The sentence contains the word 'python'.")
else:
    print("The sentence does not contain the word 'python'.")
