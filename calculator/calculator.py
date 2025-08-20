
import calcuheading
# Basic arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b   

# Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
#Calculator function
def calculator():
    first_num = float(input("Enter the first number: "))
    
    print("\nAvailable operations:")
    for symbol in operations:
        print(symbol)
    
    continue_calc = True
    while continue_calc:
        op_symbol = input("\nPick an operation: ")
        next_num = float(input("Enter the next number: "))
        
        operation_func = operations[op_symbol]
        result = operation_func(first_num, next_num)
        
        print(f"\n{first_num} {op_symbol} {next_num} = {result}")
        
        user_choice = input(
            f"\nType 'y' to continue with {result}, 'n' to start a new calculation, or 'x' to exit: "
        )
        
        if user_choice.lower() == "y":
            first_num = result
        elif user_choice.lower() == "n":
            continue_calc = False
            calculator()
        else:
            continue_calc = False
            print("\nThanks for using the calculator. Goodbye!")

print(calcuheading.logo)
calculator()
