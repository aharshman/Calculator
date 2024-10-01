# Graphical Calculator

This project is a graphical calculator application built in Python using a custom `graphics.py` library, which provides a GUI interface for simple arithmetic operations. The calculator supports basic operations like addition, subtraction, multiplication, and division.

## Features
- **Basic Operations**: Perform addition, subtraction, multiplication, and division.
- **Clear and Delete**: Clear the entire display or delete the last character.
- **Evaluate Expression**: Calculate the result of the current input.
- **Turn Off**: Close the calculator with the "OFF" button.

## Getting Started

### Prerequisites
To run this program, you need to have Python installed on your system. Additionally, the calculator uses the `graphics.py` library, which is a simplified wrapper for Tkinter. Ensure that you have the required files (`graphics.py` and `button.py`) in the same directory as the calculator script.

### Installation
1. Clone the repository or download the code files.
2. Ensure that the `graphics.py` and `button.py` files are in the same directory as the main calculator script.

### Running the Application
To run the calculator, navigate to the directory containing the script and use the following command:

'''sh
python calculator.py

## How to Use
1. Input Numbers: Click on the number buttons (0-9) to enter a value.
2. Enter Operations: Click on an operation button (+, -, *, /) to apply it to the current value.
3. Evaluate Expression: Click the = button to evaluate the current expression.
4. Clear/Correct Input:
  1. Use the C button to clear the entire display.
  2. Use the <- button to delete the last character.
5. Turn Off Calculator: Click on the OFF button to close the calculator.

## Code Structure
1. Calculator Class: The main class that defines the calculator and handles the GUI.
  1. __init__(): Initializes the calculator window and creates buttons and display.
  2. __createbuttons(): Creates the calculator buttons.
  3. __createDisplay(): Creates the display area for input and results.
  4. getbutton(): Waits for the user to click a button and returns the clicked button's label.
  5. processButton(key): Handles actions based on which button was clicked.
  6. run(): Main event loop to keep the calculator running and handle user input.

## Important Notes
1. Dependencies: This code depends on a graphics.py library for GUI rendering and a button.py module for button creation. These are not standard Python libraries and must be provided.
2. Security Warning: The calculator uses eval() to evaluate expressions, which can be risky as it may execute arbitrary code. This should be replaced with a safer alternative for real-world applications.

## Potential Improvements
1. Security: Replace eval() with a safer method, such as using the ast module (ast.literal_eval) or a math library.
2. Extended Functionality: Add support for additional mathematical operations, such as parentheses, square roots, and exponents.
3. Improved Styling: Enhance the visual appeal of the calculator by differentiating between operators and numbers with different colors.

## License
1. This project is provided as-is, without any warranty or guarantee of functionality. You are free to modify and distribute it as needed.

## Author
1. Alexander Harshman

## Acknowledgements
1. graphics.py Library: For the GUI interface, allowing easy rendering of graphical elements.
2. Python Programming: The main language used for developing the calculator.
