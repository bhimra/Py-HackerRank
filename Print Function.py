"""
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.

Example
n=5
Print the string 12345.

Input Format:
The first line contains an integer n .

Constraints::
1<=n<=150

Output Format:::
Print the list of integers from 1 through n as a string, without spaces.

Sample Input 0
3

Sample Output 0
123

"""
#use input 5, 10,133 to test case
if __name__=='__main__':
    n = int(input())
    if 1 <= n <= 150:
        number=0
        for i in range(1,n+1):
            #number=number*10+i
            print(i,end="")
    else:
        print("Please enter a number between 1 and 150.")