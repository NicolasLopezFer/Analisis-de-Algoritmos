
## -------------------------------------------------------------------------
def Bubble( S ):
    for i in range( len( S ) ):
        for j in range( len( S ) - i - 1 ):
            if S[ j + 1 ] < S[ j ]:
                aux = S[ j ]
                S[ j ] = S[ j + 1 ]
                S[ j + 1 ] = aux
            # end if
        # end for
    # end for
# end def

## -------------------------------------------------------------------------
def Insertion( S ):
    for j in range( 1, len( S ) ):
        k = S[ j ]
        i = j - 1
        while 0 <= i and k < S[ i ]:
            S[ i + 1 ] = S[ i ]
            i = i - 1
        # end while
        S[ i + 1 ] = k
    # end for
# end def

## -------------------------------------------------------------------------
def Surprise_Aux_Merge( S, b, h, e ):
    pass
# end def

## -------------------------------------------------------------------------
def Surprise_Aux( S, b, e ):
    if b < e:
        h = int( ( b + e ) / 2 )
        Surprise_Aux( S, b, h )
        Surprise_Aux( S, h + 1, e )
        ## TODO: Merge_Aux_Merge( S, b, h, e )
    # end if
# end def

## -------------------------------------------------------------------------
def Surprise( S ):
    Surprise_Aux( S, 0, len( S ) - 1 )
# end def

## eof - Sort.py

