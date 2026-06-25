def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
x = int(input("Enter 1st num: "))
y = int(input("Enter 2 num: "))
z = int(input("Enter 3 num: "))
print("Largest Number =", largest(x, y, z))