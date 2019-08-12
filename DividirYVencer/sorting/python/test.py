import time, sys
import Sort

if len( sys.argv ) < 2:
    print( "Usage: python3", sys.argv[ 0 ], "file")
    exit( 1 )
# end if

start = True
n = 0
S = []
with open( sys.argv[ 1 ] ) as fin:
    for line in fin:
        if start:
            n = int( line )
            start = False
        else:
            S.append( int( line ) )
        # end if
    # end for
# end with

bubbleS = list( S )
insertionS = list( S )
surpriseS = list( S )

start = time.time( )
Sort.Bubble( bubbleS )
bubbleT = time.time( ) - start

start = time.time( )
Sort.Insertion( insertionS )
insertionT = time.time( ) - start

start = time.time( )
Sort.Surprise( surpriseS )
surpriseT = time.time( ) - start

print( len( S ), bubbleT, insertionT, surpriseT )

## eof - Sorting.py

