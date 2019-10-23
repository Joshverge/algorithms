"""
An algorithm to compute the decimal representation of 2^n
in O(n^(lg 3)) time.
"""


def TwoToThe(n):
  if n == 0:
    return 1
  m = n // 2
  z = TwoToThe(m)
  z = z*z   # replace with karatsuba
  if n % 2 == 1:
    z = z + z
  return z


print(TwoToThe(10))
