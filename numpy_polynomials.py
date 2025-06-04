"""
To determine the coefficients of a polynomial given its sequence of roots, you can use the factorized form:
[ P(x) = (x - r_1)(x - r_2) \dots (x - r_n) ]
Where:
- ( r_1, r_2, \dots, r_n ) are the given roots of the polynomial.
- Expanding the expression will give you the coefficients.
Example:
If the roots are 2, 3, and 5, the polynomial is: [ P(x) = (x - 2)(x - 3)(x - 5) ]
Expanding step-by-step:
- Multiply first two factors: [ (x - 2)(x - 3) = x^2 - 5x + 6 ]
- Multiply the result by the last factor: [ (x3 - 10x^2 + 31x - 30 ]
So, the coefficients of the polynomial ( x2 + 31x - 30 ) are: [ [1, -10, 31, -30] 

Problem :::::::::::::::
 
Poly
The poly tool returns the coefficients of a polynomial with the given sequence of roots.
print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]

roots
The roots tool returns the roots of a polynomial with the given coefficients.
print numpy.roots([1, 0, -1])           #Output : [-1.  1.]
 
Polyint
The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]
 
Polyder
The polyder tool returns the derivative of the specified order of a polynomial.
print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]
 
Polyval
The polyval tool evaluates the polynomial at specific value.
print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34
 
Polyfit
The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.
print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]
 
The functions polyadd, polysub, polymul, and polydiv also handle proper addition, subtraction, multiplication, and division of polynomial coefficients, respectively.
 
Task :
You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.


Input Format :
The first line contains the space separated value of the coefficients in P.
The second line contains the value of x.

Output Format :
Print the desired value.


Sample Input :
1.1 2 3
0
 
Sample Output :
3.0

"""

import numpy as np  # Importing NumPy

# Read polynomial coefficients from user input
poly = [float(x) for x in input().split()]

# Read the value of x where the polynomial is evaluated
x = float(input())

# Compute and print the polynomial value at x
print(np.polyval(poly, x))

"""
How It Works
- Reading Polynomial Coefficients
- input().split() takes space-separated numbers (coefficients) from the user.
- [float(x) for x in input().split()] converts them into a list of floating-point numbers.
- Reading the Value of x
- x = float(input()) takes a floating-point value from the user.
- Evaluating the Polynomial
- np.polyval(poly, x) computes the polynomial’s value at x.
- NumPy treats poly as coefficients of a polynomial in descending order of powers.
Example Usage
Input
1 -3 2  # Coefficients for x² - 3x + 2
4       # Value of x


Processing
[ P(4) = (1 \times 4^2) + (-3 \times 4) + 2 = 16 - 12 + 2 = 6 ]
Output
6.0

Key Takeaways
- np.polyval(poly, x) is great for polynomial evaluation.
- Coefficients must be ordered from highest degree to lowest.
- x is the point where the polynomial is evaluated.
"""