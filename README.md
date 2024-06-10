# Arithmetic Expression Validator

This repository contains a Python script that validates and evaluates arithmetic expressions input by the user. The script checks if the input is a valid arithmetic expression and then evaluates it if valid. If the input is invalid, it returns an appropriate error message.

## Features

- **Validation of Arithmetic Expressions**: The script ensures the input string is a valid arithmetic expression, checking for factors such as valid characters, balanced parentheses, absence of consecutive operators, and appropriate starting/ending characters.
- **User Interaction**: Continuously prompts the user for input until the user decides to exit.
- **Error Handling**: Provides specific error messages for different types of invalid inputs.

## Usage

1. Clone the repository to your local machine.
2. Run the script using Python.

    ```sh
    python script_name.py
    ```

3. Enter an arithmetic expression when prompted. For example: `3 + (4 * 5) - 7 / 2`.
4. The script will evaluate the expression if it's valid or return an error message if it's invalid.
5. To exit the script, type `exit`.

## Example

    ```sh
    Enter your input (or 'exit' to quit): 3 + (4 * 5) - 7 / 2
    12.5
    
    Enter your input (or 'exit' to quit): (3 + 5 * 2
    Invalid input. Unbalanced parentheses.
    
    Enter your input (or 'exit' to quit): exit
    ```
## Functionality

The script defines the process_input function which performs the following checks:

    Pattern Matching: Ensures the input only contains numbers and arithmetic operator symbols (+, -, *, /, ()).
    Balanced Parentheses: Checks for balanced parentheses.
    Consecutive Operators: Detects consecutive operator symbols.
    Valid Start/End: Ensures the expression does not start or end with an operator.
    Length Check: Limits the expression length to 100 characters.
    Evaluation: If all checks pass, the expression is evaluated using Python's eval function.

## Notes

    The script uses Python's eval function to evaluate expressions, which can be a security risk if the input is not properly sanitized. Ensure the input is trusted or consider alternative evaluation methods for untrusted input.
    The script removes spaces from the input before processing, so spaces can be used freely for readability.

## Contributing

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements.
## License

This project is licensed under the MIT License. See the LICENSE file for details.
