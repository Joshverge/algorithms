# recurively output a no. in array + 1 if no. is odd; else output no. - 1
# uses two recursive fuctions to achieve this
import numpy as np

def rec1(a, i):
  if len(a) == i:
    return
  if a[i] % 2 == 1:
    a[i] +=1
    print(a[i])
    rec2(a,i+1)
  else:
    rec2(a,i)

def rec2(a, i):
  if len(a) == i:
    return
  if a[i] % 2 == 0:
    a[i] -=1
    print(a[i])
    rec1(a,i+1)
  else:
    rec1(a,i)

a = np.linspace(1,20,20)
rec2(a,0)
