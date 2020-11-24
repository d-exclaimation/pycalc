# pycalc

 Python Math, Calculus and Geometry Module

Authored by Vincent

## Quick guide:

Note: You can import all individual module by using "import module_name"

However, if you want the entirety of this module, you can just import the pycalc module which should import all the rest

# Set up:

> 1. Download the folders, and put it in the folder that you want to write code on
> 2. Import the modules ( by having import module_name )
> 3. Start using it


 e.g: 
 ```python
 import pycalc
  
 print(pycalc.Vector3.zero())
 # output should be Vector3 (0, 0, 0)
 ```

# Descriptions:

import pycalc, import all the functions, classes with the namespace pycalc (e.g: pycalc.Vector3, pycalc.permute(x, y))

import vectors, import vectors related functions and classes such as Vector2, Vector3, VectorAny, and triangle(vector_x, vector_y) function

import matrices, import matrices related functions and classes such as the Matrix itself and all it's methods

import augmented_matrix, import functions related to augmented_matrix like 2D list / array of the AugMatrix class

import probabilities, import all functions related to probabilities such as permutations, factorials, and also import the Fraction object

any more information is available in the code docstrings and comment, use help(name_of_function_or_class)
