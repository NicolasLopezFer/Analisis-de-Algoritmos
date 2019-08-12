
import random, sys, time
import Selection

## -- Create a random sequence
if len( sys.argv ) < 3:
    print( "Usage: python3", sys.argv[ 0 ], "number k")
    exit( 1 )
# end if
n = int( sys.argv[ 1 ] )
k = int( sys.argv[ 2 ] )
S = []
for i in range( n ):
    S.append( random.randint( -10000000, 10000000 ) )
# end for

t = time.time( )
m1 = Selection.Select_1( S, k )
t1 = time.time( ) - t

t = time.time( )
m2 = Selection.Select_2( S, k )
t2 = time.time( ) - t

t = time.time( )
S.sort( )
m3 = S[ k ]
t3 = time.time( ) - t

print(
    m1, m2, m3,
    S[ k - 1 ], S[ k ], S[ k + 1 ],
    "{:.3e}".format( t1 ),
    "{:.3e}".format( t2 ),
    "{:.3e}".format( t3 )
    )

## eof - experiment.py
