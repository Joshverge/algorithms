# Gauss and Laquière’s backtracking algorithm for the n queens problem
# Jeff's notes BackTracking 73

count =0

def placeQ(Q, r, n):
  global count
  if r == n:
    count = count + 1
    print(Q)
  else:
    for j in range(0,n):
      legal = 1
      for i in range(0, r):
        if Q[i]==j or Q[i]==j+r-i or Q[i]==j-r+i:
          legal = 0
      if legal:
        # print(r)
        Q[r] = j
        placeQ(Q, r+1, n)


n = 10
Q = [0]*n
placeQ(Q, 0, n)
print("No. of solutions:", count)
