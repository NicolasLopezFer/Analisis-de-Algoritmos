#ifndef __sort_algos__hxx__
#define __sort_algos__hxx__

#include <iterator>

// -------------------------------------------------------------------------
template< class _TIterator >
void BubbleSort( _TIterator begin, _TIterator end )
{
  for(
    auto i = std::make_reverse_iterator( end );
    i != std::make_reverse_iterator( begin );
    ++i
    )
  {
    _TIterator e = i.base( );
    for( _TIterator j = begin; j != e; ++j )
    {
      _TIterator k = j;
      k++;
      if( k != e )
      {
        if( *k < *j )
        {
          auto aux = *j;
          *j = *k;
          *k = aux;
        } // end if
      } // end if
    } // end for
  } // end for
}

// -------------------------------------------------------------------------
template< class _TIterator >
void InsertionSort( _TIterator begin, _TIterator end )
{
  _TIterator j = begin;
  j++;
  for( ; j != end; ++j )
  {
    auto k = *j;
    auto i = std::make_reverse_iterator( j );
    auto e = std::make_reverse_iterator( begin );
    while( i != e && k < *i )
    {
      *i =
    } // end while
    *i = k;

  } // end for

  /* TODO
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
     } // end while
     S[ i + 1 ] = k;
     } // end for
  */
}

#endif // __sort_algos__hxx__

// eof - sort_algos.hxx
