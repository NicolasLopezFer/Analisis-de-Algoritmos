#ifndef __sort_algos__h__
#define __sort_algos__h__

/* ----------------------------------------------------------------------
 * Inputs  : "begin" and "end" are iterators over the input sequence
 * Outputs : "begin" and "end" are iterators over the modified sequence,
 *           that has been permutated to be ordered.
 * ----------------------------------------------------------------------
 */
template< class _TIterator >
void BubbleSort( _TIterator begin, _TIterator end );

/* ----------------------------------------------------------------------
 * Inputs  : "begin" and "end" are iterators over the input sequence
 * Outputs : "begin" and "end" are iterators over the modified sequence,
 *           that has been permutated to be ordered.
 * ----------------------------------------------------------------------
 */
template< class _TIterator >
void InsertionSort( _TIterator begin, _TIterator end );

#include "sort_algos.hxx"

#endif // __sort_algos__h__

// eof - sort_algos.h
