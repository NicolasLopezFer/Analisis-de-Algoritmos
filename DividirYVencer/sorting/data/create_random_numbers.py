
import random, sys

if len( sys.argv ) < 2:
    print( "Usage: python3", sys.argv[ 0 ], "number")
    exit( 1 )
# end if
n = int( sys.argv[ 1 ] )
print( n )
for i in range( n ):
    print( random.randint( -10000, 10000 ) )
# end for

## eof - Sorting.py

