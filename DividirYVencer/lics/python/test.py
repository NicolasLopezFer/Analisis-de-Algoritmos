
import LICS

# S = [ 1, 2, 3, 0, -1, 2, 8, 9, 11, 300 ]
# S = [ 9, 7, 7, 1, 2, 3, 4, 6, 5 ]
# S = [9567, 8105, -9383, 3226, -2941, -3790, 9307, 6770, 7413, 1106]


bf = LICS.BruteForce( S )
dc = LICS.DivideAndConquer( S )

print( "Brute force       :", bf )
print( "Divide and conquer:", dc )

## eof - test.py