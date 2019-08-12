import math
import random
import time
def MaxCrossSubArray( A , l , m , h ):
    vl=-math.inf
    s=0
    ml=0
    for i in range(m,l,-1):
        s=s+A[i]
        if s>vl:
            vl=s
            ml=i
        #endif
    #endfor
    vr=-math.inf
    s=0
    mr=0
    for i in range(m+1,h):
        s=s+A[i]
        if s>vr:
            vr=s
            mr=i
        #endif
    #endfor
    return[ml,mr,vl+vr]
#enddef
def MaxSubArray(A,l,h):
    if h<=l:
        return [l ,h ,A[l]]
    else:
        m=int((l+h)/2)
        [ll,lh,ls] = MaxSubArray(A,l,m)
        [rl,rh,rs] = MaxSubArray(A,m+1,h)
        [cl,ch,cs] = MaxCrossSubArray(A,l,m,h)
        if ls>=rs and ls>=cs:
            return [ll,lh,ls]
        elif rs>=ls and rs>=cs:
            return [rl,rh,rs]
        else:
            return [cl,ch,cs]

#enddef
def MaxProfit_DC( S ):
    A=[0]
    for i in range(1, len(S)):
        A.append( S[i]-S[i-1])
    #endfor
    return MaxSubArray(A,1,len(S)-1)
#enddef
def MaxProfit_BF( S ):
    minI=0
    maxI=0
    maxP= -math.inf 
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            p=S[j]-S[i]
            if p>maxP:
                minI=i
                maxI=j
                maxP=p
            #endif
        #endfor
    #endfor
    return [minI,maxI,maxP]
#enddef

#S=[100,113,110,85,1045,102,86,63,57,101,79,94,90,97]
S=[]
for i in range(200000):
    S.append(random.uniform(0.1,100000))

start=time.time()
[i1,j1,p1]=MaxProfit_BF(S)
bfT=time.time()-start
start=time.time()
[i2,j2,p2]=MaxProfit_DC(S)
dcT=time.time()-start
print(bfT,dcT)
print(i1,i2-1,j1,j2,p1,p2)