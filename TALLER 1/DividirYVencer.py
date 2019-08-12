def MMRotado(S,l,h):

  if h < l:
    return [0,-1]
  #endif
  elif h == l:
    return [S[l],S[h]]
  #endif
  elif h==1:
    return [S[0],S[1]]
  #endif
  elif S[0]>S[1]:
    return [S[0],S[1]]
  else:
    if(h==2):
      S.append(S[len(S)-1])
      h = h + 1
    #endif
    mitad = int((h+l)//2)
    if(S[mitad] > S[mitad-1]):
      aux = S[mitad:len(S)+1]
      return MMRotado(aux,0,len(aux)-1)
    #endif
    if(S[mitad] < S[mitad+1]):
      aux = S[0:mitad+1]
      return MMRotado(aux,0,mitad)
    #endif
    return [0,0]


def MaxMinRotadoDV(S):
  return MMRotado(S,0,len(S)-1)
