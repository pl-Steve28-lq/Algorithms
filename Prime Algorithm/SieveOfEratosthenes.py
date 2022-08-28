def primeSieve(n):
  sieve = [0]*2 + [1]*(n-1)
  for i in range(2, int(n**.5)+1):
    if sieve[i]:
      sieve[i*2::i] = [0] * (n//i-1)
  return [x for x, s in enumerate(sieve) if s]
