def FastRecFibo(n):
  if n == 1:
    return 0, 1
  m = int(n//2)
  hprv, hcur = FastRecFibo(m)
  prev = hprv*hprv + hcur*hcur
  cur = hcur*(2*hprv + hcur)
  next = prev + cur
  if n % 2 == 0:
    return prev, cur
  else:
    return cur, next

print(FastRecFibo(50))
