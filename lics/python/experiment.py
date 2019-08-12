import time, random, sys
import LICS

if len( sys.argv ) < 2:
    print( "Usage: python3", sys.argv[ 0 ], "length")
    exit( 1 )
# end if
n = int( sys.argv[ 1 ] )
S = []
for i in range( n ):
    S.append( random.randint( -10000, 10000 ) )
# end for

start = time.time( )
bfL = LICS.BruteForce( S )
bfT = time.time( ) - start

start = time.time( )
dcL = LICS.DivideAndConquer( S )
dcT = time.time( ) - start

bfIsOrdered = ( bfL == sorted( bfL ) )
dcIsOrdered = ( dcL == sorted( dcL ) )

print( "Original length            :", len( S ) )
print( "Brute force length         :", len( bfL ) )
print( "Divide and conquer length  :", len( dcL ) )
print( "Brute force ordered?       :", bfIsOrdered )
print( "Divide and conquer ordered?:", dcIsOrdered )
print( "Brute force time           :", bfT )
print( "Divide and conquer time    :", dcT )

if len( bfL ) != len( dcL ):
    print( S )
    print( bfL )
    print( dcL )
# end fi    

## eof - Sorting.py

