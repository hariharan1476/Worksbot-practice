def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
nu = int(input("Enter a number: "))
if is_prime(nu):
    print(nu, "is a Prime Number")
else:
    print(nu, "is not a Prime Number")