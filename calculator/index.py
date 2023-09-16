def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


choice = input("Enter the operation number (1/2/3/4): ")


if choice not in ('1', '2', '3', '4'):
    print("Invalid input")
else:
  
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        operation = "Addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "Multiplication"
    else:
        result = divide(num1, num2)
        operation = "Division"

  
    print(f"{operation} result: {result}")
