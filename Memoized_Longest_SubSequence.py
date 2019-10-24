import numpy as np

# float("inf")
def LIS(A):
  n = len(A) - 1
  A[0] = -10**3
  LIS_ = np.zeros((n+1,n+2))
  for i in range(0,n+1):
    LIS_[i, n+1] = 0

  for j in range(n, 0, -1):
    for i in range(j-1, -1, -1):
      # print("i:",i, " j:",j)
      if A[i] >= A[j]:
        LIS_[i, j] = LIS_[i, j+1]
      else:
        LIS_[i, j] = max(LIS_[i,j+1], 1 + LIS_[j, j+1])
    print("After one col:")
    print(LIS_)
  return LIS_[0,1]

a = [0,1,33,4]
print(LIS(a))
