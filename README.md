# Polar Coordinates
This python script allows you to input a mathmatical function in polar coordinates and visualizes the corresponding plot. The user given function is given through the command line. The program accepts standard mathmatical functions such as addition, subtraction, multiplication, division, square roots, exponents, and trigonometric fuctions like sine and cosine.

## Features
Parse and evaluate mathematical functions in polar coordinates.
Support for functions: Addition, Subtraction, Multiplication, Division, Square Root, Exponentiation, Cosine, Sine.
Supports x as a variable for plotting parametric equations.
Plots the function in polar coordinates using matplotlib.
Allows for easy input of mathematical expressions and visual representation.
Installation
To use the Polar Function Plotter, you need Python and matplotlib and numpy installed on your system. You can install the required dependencies using pip:

```bash
pip install matplotlib numpy
```
## Usage
1) Clone this repository or download the script to your local machine.
2) Open a terminal or command prompt and navigate to the directory where Polar.py is located.
3) Run the script using Python:
```bash
python Polar.py
```
4) The script will prompt you to enter a mathematical function in the format y=<yourFunction>.
5) Once you input your function, the script will parse the function, compute the corresponding range values, and plot the result on a graph.
### Example Input:
```bash
Input: y=cos(x)
```
### Example Output:
A plot of the cosine function in polar coordinates.

## Functions Supported
- Arithmetic Operations: +, -, *, /
- Square Root: sqrt
- Exponentiation: ^
- Trigonometric Functions: cos(x), sin(x)
- Parentheses: () for grouping terms
  
## How it Works
The user inputs a mathematical function in the form y=<yourFunction>.
The function is parsed into components (numbers, variables, functions, operators).
The function is then evaluated over a specified domain, and the corresponding range values are calculated.
These values are converted to Cartesian coordinates, and a plot is generated using matplotlib.
### Example
Input: y=sin(x)

Output: A plot of the sine wave in polar coordinates.

## Contributing
Feel free to open issues or submit pull requests for enhancements, bug fixes, or additional features.

## License
This project is open-source and available under the MIT License.
