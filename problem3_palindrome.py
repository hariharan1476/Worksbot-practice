def palindrome(text):
    return text == text[::-1]
w = input("Enter a word: ")
if palindrome(w):
    print("Palindrome")
else:
    print("Not Palindrome")