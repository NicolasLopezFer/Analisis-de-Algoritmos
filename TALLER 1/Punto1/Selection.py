def Select(S,menor,mayor,k):
  if mayor < menor:
    return -1
  #endif
  else:
    lista = []
    aux = []
    columna = 0
    if len(S) >= 4:
      for i in range (len(S)):
        for j in range (5):
          aux=S[i]

def MediSelection(S,k):
  menor = 0
  mayor = len(S)-1;
  return Select(S,menor,mayor,k)
#end def


S = [2,5,3,1,7,9,10,16,13,4,8,6,11,12,14,15]
k = 5
media = MediSelection(S,k)
print(media);
