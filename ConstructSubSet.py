#Recursive algorithm to find subset that sums to T in set X of POSITIVE integers
#Assume 0 is part of every set i.e empty set is part of every set

def constructSubSet(X,i,T):
  if T == 0:
    return set([])
  elif T < 0 or i == 0:
    return None
  else:
    for x in X:
      X_copy = X.copy()
      X_copy.discard(x)
      Y_1 = constructSubSet(X_copy, i-1, T)
      if Y_1 != None:
        return Y_1
      Y_2 = constructSubSet(X_copy, i-1, T - x)
      if Y_2 != None:
        Y_2.add(x)
        return Y_2
    return None

X = set([2,4,5,7,8,10])
T = 21
print(constructSubSet(X, 6, T))
