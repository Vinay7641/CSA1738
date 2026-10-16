a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
ch = int(input("Enter choice: "))
if ch == 1:
    print("Result =", a + b)
elif ch == 2:
    print("Result =", a - b)
elif ch == 3:
    print("Result =", a * b)
elif ch == 4:
    print("Result =", a / b)
else:
    print("Invalid choice")