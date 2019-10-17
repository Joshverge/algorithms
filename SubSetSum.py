#Recursive algorithm to find sum T in set X of POSITIVE integers
#Assume 0 is part of every set i.e empty set is part of every set
# T(n) = 2T(n-1) + O(1) -> O(2^n) runtime

def subSetSum(X,T):
  if T == 0:
    return True
  elif T < 0 or not X:
    return False
  else:
    for x in X:
      X_copy = X.copy()
      X_copy.discard(x)
      With = subSetSum(X_copy, T - x)
      Without = subSetSum(X_copy, T)
      return With or Without


X = set([2,4,5,7,8,10])
T = 26

print(subSetSum(X,T))
