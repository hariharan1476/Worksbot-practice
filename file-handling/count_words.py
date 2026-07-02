try:
    with open("sample.txt", "r") as file:
        content = file.read()

    words = content.split()

    print("Total Words:", len(words))
    print("Total Characters:", len(content))

except Exception as e:
    print("Error:", e)