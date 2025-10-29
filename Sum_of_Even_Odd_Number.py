# Python program to find out
# Sum of elements at even and 
# odd index positions separately using bitwise & operator

# Function to calculate Sum
def EvenOddSum(a, n):
    even = 0
    odd = 0
    for i in range(n):

        # Loop to find even, odd Sum
        if i &1:
            odd += a[i]
        else:
            even += a[i]
    
    print ("Even index positions sum ", even)
    print ("Odd index positions sum ", odd)

# Driver Function

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)

EvenOddSum(arr, n)

# This code is contributed by tvsk
