try:
    with open("sample.txt", "r") as source:
        content = source.read()

    with open("copy_sample.txt", "w") as destination:
        destination.write(content)

    print("File copied successfully.")

except Exception as e:
    print("Error:", e)