import math

## -------------------------------------------------------------------------
def BruteForce( S ):
    maxS = -math.inf
    maxI = -1
    maxJ = -1
    for i in range( len( S ) ):
        for j in range( i, len( S ) ):
            isOrdered = True
            for k in range( i + 1, j + 1 ):
                if S[ k ] <= S[ k - 1 ]:
                    isOrdered = False
                # end if
            # end for
            if isOrdered and maxS < ( j - i ):
                maxS = j - i
                maxI = i
                maxJ = j
            # end if
        # end for
    # end for
    return S[ maxI : maxJ + 1 ]
# end def

## -------------------------------------------------------------------------
def DivideAndConquerPivot( S, b, q, e ):
    i = q
    while b < i and S[ i - 1 ] <= S[ i ]:
        i = i - 1
    # end while
    j = q
    while j < e and S[ j ] <= S[ j + 1 ]:
        j = j + 1
    # end while
    return [ i, j ]
# end def

## -------------------------------------------------------------------------
def DivideAndConquerAux( S, b, e ):
    if e < b:
        return [ 0, -1 ]
    elif e == b:
        return [ b, b ]
    else:
        q = int( ( b + e ) / 2 )
        [ Li, Lj ] = DivideAndConquerAux( S, b, q - 1 )
        [ Ri, Rj ] = DivideAndConquerAux( S, q + 1, e )
        [ Ci, Cj ] = DivideAndConquerPivot( S, b, q, e )
        if ( ( Lj - Li ) > ( Rj - Ri ) ) and ( ( Lj - Li ) > ( Cj - Ci ) ):
            return [ Li, Lj ]
        elif ( ( Rj - Ri ) > ( Lj - Li ) ) and ( ( Rj - Ri ) > ( Cj - Ci ) ):
            return [ Ri, Rj ]
        else:
            return [ Ci, Cj ]
        # end if
    # end if
# end def

## -------------------------------------------------------------------------
def DivideAndConquer( S ):
    [ i, j ] = DivideAndConquerAux( S, 0, len( S ) - 1 )
    return S[ i : j + 1 ]
# end def

## eof - LICS.py
