#include "sort_algos.h"

/* ---------------------------------------------------------------------- */
void BubbleSort( long* S, long n )
{
  long i, j;
  long aux;

  for( i = n - 1; 0 <= i; i-- )
  {
    for( j = 0; j < i; j++ )
    {
      if( S[ j + 1 ] < S[ j ] )
      {
        aux = S[ j ];
        S[ j ] = S[ j + 1 ];
        S[ j + 1 ] = aux;
      } /* end if */
    } /* end for */
  } /* end for */
}

/* ---------------------------------------------------------------------- */
void InsertionSort( long* S, long n )
{
  long i, j;
  long k;

  for( j = 1; i < n; i++ )
  {
    k = S[ j ];
    i = j - 1;
    while( 0 <= i && k < S[ i ] )
    {
      S[ i + 1 ] = S[ i ];
      i--;
    } /* end while */
    S[ i + 1 ] = k;
  } /* end for */
}

/* eof - sort_algos.c */
