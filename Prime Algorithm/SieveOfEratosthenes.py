def primeSieve(n):
  sieve = [False]*2 + [True]*(n-1)
  for idx, e in enumerate(seive):
    if e:
      k = idx*2
      while k <= n:
        seive[k] = False
        k += idx
  return [x for (x, y) in enumerate(seive) if y]

def primeSieveWithSlicing(n):
  sieve = [False]*2 + [True]*(n-1)
  for i in range(2, int(n**.5 + 1.5)):
    if sieve[i]:
      sieve[i*2::i] = [False] * ((n-i) // i)
  return [x for x in range(n+1) if sieve[x]]
