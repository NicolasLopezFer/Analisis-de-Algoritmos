import time, sys
import random

def Swap(S,a,b):
    temp = S[a]
    S[a] = S[b]
    S[b] = temp

def Partition(S,p,r):
    x = S[r]
    i = p - 1
    j = p
    for j in range(r-1):
        if S[j] <= x:
            i = i + 1
            Swap(S,i,j)
        #end if
    #end for
    Swap(S,i+1,r)
    return i+1
#end def

def Randomizedpartition(S,p,r):
    i = random.randint(p,r)
    Swap(S,r,i)
    return Partition(S,p,r)

def QuickSort_Aux(S,p,r):
    if p < r:
        q = Randomizedpartition(S,p,r)
        QuickSort_Aux(S,p,q-1)
        QuickSort_Aux(S,q+1,r)
    #End if
#End def

def QuickSort(S):
    QuickSort_Aux(S,1,len(S))

S=[50,20,39,84,12,56,102,564,231,43,21,9,2,4,7,2,1,666]

start = time.time( )
QuickSort(S)
surpriseT = time.time( ) - start

print(surpriseT)
