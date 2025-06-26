def main():
    print("Hello, World!")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    
    # Simple calculator
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The sum is: {result}")

if __name__ == "__main__":
    main()