def count_vowels(text):
    vow = "aeiouAEIOU"
    ct = 0
    for ch in text:
        if ch in vow:
            ct += 1
    return ct
sentence = input("Enter a string")

print("Num of vowels =", count_vowels(sentence))