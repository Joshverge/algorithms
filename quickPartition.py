a = [0,33,12,4,10,9,6,5]

def Partition(a):
  pivot = len(a)-1
  i = 0
  for j in range(len(a)-1):
    if a[j] < a[pivot]:
      swap(a ,j ,i)
      i +=1
  swap(a, pivot, i)


def swap(a, i ,j):
  a[i], a[j] = a[j], a[i]


Partition(a)
print(a)
# print(hex(id(a)))
# print(hex(id(b)))
