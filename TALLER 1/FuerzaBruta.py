def MaxMinRotadoFB(S):
  maxi = 0
  mini = 0
  for i in range(len(S)):
    if S[i] > maxi:
      maxi = S[i]
    #endif
  #endfor
  mini = maxi
  i = 0
  for j in range(len(S)):
    if S[j] < mini:
      mini = S[j]
    #endif
  #endfor
  return [maxi,mini]
#enddef
