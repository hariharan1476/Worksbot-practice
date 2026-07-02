try:
    with open("sample.txt", "w") as file:
        file.write("Welcome to Python File Handling.\n")
        file.write("This file is created using Python.\n")

    print("File written successfully.")

except Exception as e:
    print("Error:", e)