def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
cou = int(input("Enter no of terms: "))
fibonacci(cou)