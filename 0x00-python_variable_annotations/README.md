0x00. Python - Variable Annotations

Type annotations in Python 3
Usage of type annotations in specifying function signatures and variable types
Duck typing and its use cases
Code validation using mypy

Requirements
Editor: vi, vim, emacs
OS: Ubuntu 18.04 LTS with Python 3.7
Coding Style: PEP 8 style (version 2.5.x)
Documentation: Each module, class, and function must be properly documented

Tasks
0. Basic annotations - add
Create a type-annotated function add that takes two floats and returns their sum as a float.

1. Basic annotations - concat
Develop a type-annotated function concat that concatenates two strings.

2. Basic annotations - floor
Implement a type-annotated function floor that returns the floor of a float.

3. Basic annotations - to string
Write a type-annotated function to_str that takes a float and returns its string representation.

4. Define variables
Define and annotate the following variables with the specified values:

5. Complex types - list of floats
Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.

6. Complex types - mixed list
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.

7. Complex types - string and int/float to tuple
Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.

8. Complex types - functions
Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

9. Let's duck type an iterable object
Annotate the below function’s parameters and return values with the appropriate types

Advance tasks
10. Duck typing - first element of a sequence
Augment the following code with the correct duck-typed annotations:

11. More involved type annotations
Given the parameters and the return values, add type annotations to the function
Hint: look into TypeVar

12. Type Checking
Use mypy to validate the following piece of code and apply any necessary changes.

Author:  Philip Ajuong Deng
