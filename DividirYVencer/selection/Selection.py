import math, random

## ---------------------------------------------------------------------
def Merge( S, b, q, e ):
    L = S[ b : q + 1 ]
    R = S[ q + 1 : e + 1 ]
    L.append( math.inf )
    R.append( math.inf )
    i = 0
    j = 0
    for k in range( b, e + 1 ):
        if L[ i ] < R[ j ]:
            S[ k ] = L[ i ]
            i = i + 1
        else:
            S[ k ] = R[ j ]
            j = j + 1
        # end if
    # end for
# end def

## ---------------------------------------------------------------------
def MergeSort( S, b, e ):
    if b < e:
        q = int( ( b + e ) / 2 )
        MergeSort( S, b, q )
        MergeSort( S, q + 1, e )
        Merge( S, b, q, e )
    # end if
# end def

## ---------------------------------------------------------------------
def Partition( S, p, r ):
    x = S[ r ]
    i = p - 1
    for j in range( p, r ):
        if S[ j ] <= x:
            i = i + 1
            a = S[ i ]
            S[ i ] = S[ j ]
            S[ j ] = a
        # end if
    # end for
    a = S[ i + 1 ]
    S[ i + 1 ] = S[ r ]
    S[ r ] = a
    return i + 1
# end def

## ---------------------------------------------------------------------
def RendomizedPartition( S, p, r ):
    i = random.randint( p, r )
    a = S[ i ]
    S[ i ] = S[ r ]
    S[ r ] = a
    return Partition( S, p, r )
# end def

## ---------------------------------------------------------------------
def Select_1( S, k ):
    T = list( S )
    MergeSort( T, 0, len( T ) - 1 )
    return T[ k % len( T ) ]
# end def

## ---------------------------------------------------------------------
def Select_2_Aux( S, p, r, k ):
    if p >= r:
        return S[ p ]
    else:
        q = RendomizedPartition( S, p, r )
        i = q - p + 1
        if k == i:
            return S[ q ]
        elif k < i:
            return Select_2_Aux( S, p, q - 1, k )
        else:
            return Select_2_Aux( S, q + 1, r, k - i )
        # end if
    # end if
# end def

## ---------------------------------------------------------------------
def Select_2( S, k ):
    T = list( S )
    return Select_2_Aux( T, 1, len( T ) - 1, k % len( T ) )
# end def

## eof - Selection.py

