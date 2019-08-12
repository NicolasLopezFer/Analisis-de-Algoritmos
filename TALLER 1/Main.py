import time,sys
import FuerzaBruta, DividirYVencer
import random

#S = [67,89,90,23,25,34,50,60]

with open('prueba.txt', 'w') as f:
    for i in range(1,1500):
        S=[]
        for j in range(i):
            S.append(random.uniform(1,1000))
        #endfor
        S=sorted(S)
        for k in range(0, 3):
            first = S[0];
            for q in range(0, len(S)-1):
                S[q] = S[q+1]
            S[len(S)-1] = first
        #endfor
        start = time.time()
        [max,min]= DividirYVencer.MaxMinRotadoDV(S)
        timed = time.time()-start

        start = time.time()
        [max1,min1] = FuerzaBruta.MaxMinRotadoFB(S)
        timef = time.time()-start

        linea = [i,timed,timef]
        for item in linea:
            f.write("%s " % item)
        #endfor
        f.write("\n")
    #endfor
#endwith
