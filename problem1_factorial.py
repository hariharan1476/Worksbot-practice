def factorial(n):
    fa = 1
    for i in range(1, n + 1):
        fa *= i
    return fa
nu = int(input("Enter a num: "))
print("Factorial =", factorial(nu))