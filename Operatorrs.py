# calculator program
import operator
from tkinter import N

from cv2 import multiply


Num_1 = int(input("Enter your first number: "))
# operation = input("Enter operation: ")
Num_2 = int(input("Enter your second number: "))
"""normal arithematic opeerators"""
# +	Addition	x + y
sum = Num_1 + Num_2
print(sum)
# -	Subtraction	x - y
Minus = Num_1 - Num_2
print(Minus)
# *	Multiplication	x * y
multiply = Num_1 * Num_2
print(multiply)
# /	Division	x / y
division = Num_1 / Num_2
print(division) # answer will be in float
# %	Modulus	x % y
modulus = Num_1 % Num_2
print(modulus)	
# **	Exponentiation	x ** y	
expo = Num_1 ** Num_2
print(expo) # rised to power of 1
# //	Floor division	x // y
div = Num_1 // Num_2
print(div) # 
