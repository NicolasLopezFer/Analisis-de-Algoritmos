
#include <iostream>
#include <vector>

#include "sort_algos.h"

// -------------------------------------------------------------------------
template< class _TIterator >
void Print( _TIterator begin, _TIterator end )
{
  typedef std::iterator_traits< _TIterator >  _TTraits;
  typedef typename _TTraits::value_type       _TValue;
  typedef std::ostream_iterator< _TValue >    _TOIterator;

  std::cout << "Sequence: ";
  std::copy( begin, end, _TOIterator( std::cout, " : " ) );
  std::cout << std::endl;
}

// -------------------------------------------------------------------------
int main( int argc, char* argv[] )
{
  int a[] = { 1, 4, 1, 8, 2, 7, 1, 0, 9, 9, -10 };
  Print( a, a + 11 );
  BubbleSort( a, a + 11 );
  Print( a, a + 11 );

  std::vector< double > b;
  b.push_back( 3.14 );
  b.push_back( 1.28 );
  b.push_back( -1e45 );
  b.push_back( 1e-45 );
  Print( b.begin( ), b.end( ) );
  BubbleSort( b.begin( ), b.end( ) );
  Print( b.begin( ), b.end( ) );
  return( 0 );
}

// eof - test.cxx
