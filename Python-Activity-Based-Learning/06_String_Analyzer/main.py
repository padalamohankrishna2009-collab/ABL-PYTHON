text = input("Enter a sentence: ")

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

if "python" in text.lower():
    print("The sentence contains the word 'python'.")
else:
    print("The sentence does not contain the word 'python'.")
