try:
    with open("sample.txt", "a") as file:
        file.write("Appending a new line.\n")

    print("Data appended successfully.")

except Exception as e:
    print("Error:", e)