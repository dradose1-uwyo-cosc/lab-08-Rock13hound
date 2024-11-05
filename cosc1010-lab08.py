# Elijah Gertsch
# UWYO COSC 1010
# Submission Date 11/05/2024
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def converter(value):
    try:
        int_value = int(value)
        return int_value
    except ValueError:
        pass
    try:
        float_value = float(value)
        if value.count('.') == 1 and len(value.split('.')[1]) == 1:
            return float_value
        else:
            return False
    except ValueError:
        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, x_lower, x_upper):
    if x_lower > x_upper:
        return False
    if not isinstance(x_lower, int) or not isinstance(x_upper, int):
        return False
    y_values = []
    for x in range(x_lower, x_upper + 1):
        y = m * x + b
        y_values.append(y)  
    return y_values
def get_input():
    while True:
        m_input = input("Enter slope (m) or 'exit' to quit: ")
        if m_input.lower() == 'exit':
            break       
        b_input = input("Enter intercept (b): ")
        if b_input.lower() == 'exit':
            break       
        x_lower_input = input("Enter lower x bound: ")
        if x_lower_input.lower() == 'exit':
            break       
        x_upper_input = input("Enter upper x bound: ")
        if x_upper_input.lower() == 'exit':
            break       
        try:
            m = float(m_input)
            b = float(b_input)
            x_lower = int(x_lower_input)
            x_upper = int(x_upper_input)
            result = slope_intercept(m, b, x_lower, x_upper)
            if result:
                print("Y values in given domain:", result)
            else:
                print("Invalid bounds")
        except ValueError:
            print("Invalid input. please enter only integers.")
get_input()

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

import math
def squareroot(value):
    if value < 0:
        return None
    return math.sqrt(value)
def quadratic_formula(a, b, c):
    Root = b**2 - 4*a*c
    sqrt_root = squareroot(Root)  
    if sqrt_root is None:
        return None
    x1 = (-b + sqrt_root) / (2 * a)
    x2 = (-b - sqrt_root) / (2 * a)    
    return (x1, x2)
def get_input():
    while True:
        a_input = input("Enter value for 'a' (or 'exit' to quit): ")
        if a_input.lower() == 'exit':
            break        
        b_input = input("Enter value for 'b': ")
        if b_input.lower() == 'exit':
            break        
        c_input = input("Enter value for 'c': ")
        if c_input.lower() == 'exit':
            break       
        try:
            a = float(a_input)
            b = float(b_input)
            c = float(c_input)            
            result = quadratic_formula(a, b, c)            
            if result is None:
                print("No real solutions. You can't squareroot a Negative.")
            else:
                x1, x2 = result
                print(f"The solutions to the equation are: x1 = {x1} and x2 = {x2}")        
        except ValueError:
            print("Invalid input. Please enter integer values")
get_input()
