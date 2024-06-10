import re

"""
This function takes a string as input and checks if it is a valid arithmetic expression.
The function will return True if the input is a valid arithmetic expression, and False otherwise.
True will result in the script processing the equation, while False will result in an error message.
Continuing the script will prompt the user to enter another input.
"""

def process_input(input_str):
    # Define a regular expression pattern to match numbers and operator symbols
    pattern = r'^[0-9+\-*/()]+$'
    
    # Check if the input matches the pattern
    if not re.match(pattern, input_str):
        return False, "Invalid input. Please enter a valid arithmetic expression."
    
    # Check for unbalanced parentheses
    if input_str.count('(') != input_str.count(')'):
        return False, "Invalid input. Unbalanced parentheses."
    
    # Check for consecutive operators
    if re.search(r'[+\-*/]{2,}', input_str):
        return False, "Invalid input. Consecutive operators."
    
    # Check if expression starts or ends with an operator
    if re.search(r'^[+\-\*/]|[+\-\*/]$', input_str):
        return False, "Invalid input. Expression cannot start or end with an operator."
    
    # Check if expression is too long
    if len(input_str) > 100:
        return False, "Invalid input. Expression is too long."
    
    # Evaluate the arithmetic expression
    return eval(input_str), None

# Main loop to take user input
while True:    
    # Take user input
    input_str = input("Enter your input (or 'exit' to quit): ")

    # Remove spaces from the input string
    input_str = input_str.replace(" ", "")
    
    # Check if the user wants to exit
    if input_str.lower() == 'exit':
        break
    
    # Process the input
    result, error = process_input(input_str)

    # Print the result or error message
    if error:
        print(error)
    else:
        print(result)
