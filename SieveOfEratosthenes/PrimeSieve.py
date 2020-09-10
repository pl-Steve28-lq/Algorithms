def primesieve(n):
    if n==2: return [2]
    t = list(range(2,n+1))
    for i in primesieve(n-1):
        t = list(filter(lambda x:not(x!=i and x%i==0),t))
    return t
