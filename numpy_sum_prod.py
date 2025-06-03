"""sum

The sum tool returns the sum of array elements over a given axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10
By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

prod

The prod tool returns the product of array elements over a given axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.

Task

You are given a 2-D array with dimensions NxM.
Your task is to perform the  tool over axis 0 and then find the  of that result.

Input Format

The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

Output Format
Compute the sum along axis . Then, print the product of that sum.

Sample Input
2 2
1 2
3 4

Sample Output
24

Explanation
The sum along axis  = [4 6]
The product of this sum = 24


"
In NumPy, 2D array operations like summation and product computation work efficiently using built-in functions. Here's how the logic works:

### **Summation (`numpy.sum`)**
The `numpy.sum()` function calculates the sum of array elements over a given axis:
- **`axis=0` (column-wise sum)**: Adds all values in each column.
- **`axis=1` (row-wise sum)**: Adds all values in each row.
- If no axis is specified, it sums up all elements in the entire array.

Example:
```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])

print(np.sum(arr, axis=0))  # Output: [4 6] (column-wise sum)
print(np.sum(arr, axis=1))  # Output: [3 7] (row-wise sum)
print(np.sum(arr))          # Output: 10 (sum of all elements)
```

### **Product (`numpy.prod`)**
The `numpy.prod()` function calculates the product of array elements:
- **`axis=0`**: Multiplies elements in each column.
- **`axis=1`**: Multiplies elements in each row.
- If no axis is provided, it multiplies all elements.

Example:
```python
print(np.prod(arr, axis=0))  # Output: [3 8] (column-wise product)
print(np.prod(arr, axis=1))  # Output: [2 12] (row-wise product)
print(np.prod(arr))          # Output: 24 (product of all elements)
```

### **Combining Sum and Product**
To compute the product of the sum result, you apply `numpy.prod()` to the `numpy.sum()` output:
```python
sum_result = np.sum(arr, axis=0)  # [4 6]
prod_result = np.prod(sum_result) # 4 * 6 = 24
print(prod_result)  # Output: 24
"
"""

import numpy as np
x,y = map(int, input().split())
my_arr = np.array([list(map(int, input().split())) for _ in range(x)])

sum = np.sum(my_arr,axis = 0 )

prod = np.prod(sum)
print(prod)