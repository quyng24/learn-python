def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("What is the first number?: "))
for symbol in operations:
    print(symbol)
operations_symbol = float(input("Pick an operation: "))
num2 = input("What is the next number?: ")

answer = operations[operations_symbol](num1, num2)

print(f"{num1} {operations_symbol} {num2} = {answer}")
