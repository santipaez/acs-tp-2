def main():
    print("Hello, World!")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    
    # Enhanced calculator
    print("\n--- Calculator ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    operation = input("Choose operation (+, -, *, /): ")
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Invalid operation!")
        return
    
    print(f"The result is: {result}")
    
    # Age calculator
    print("\n--- Age Info ---")
    age = int(input("Enter your age: "))
    birth_year = 2024 - age
    print(f"You were born approximately in {birth_year}")

if __name__ == "__main__":
    main()