'''
O(N logN) Time Complexity
    N     best time
   500  | 0.062 sec
  10000 | 3.068 sec
  50000 | 14.15 sec
'''

from numpy import zeros, array, cos, round
pi = 3.141592

zero = lambda n: zeros(n, dtype=complex)

def fft(p, w):
    n = p.size
    if n == 1: return p
    even = zero(n>>1)
    odd = zero(n>>1)
    
    i = 0
    while i < n:
        if i&1: odd[i>>1] = p[i]
        else: even[i>>1] = p[i]
        i += 1

    odd = fft(odd, w*w)
    even = fft(even, w*w)
    
    wp = 1+0j
    i = 0
    while i < n/2:
        e = even[i]
        o = odd[i]
        p[i] = e+wp*o
        p[i+n//2] = e-wp*o
        
        wp *= w
        i += 1
    return p

def mul(a, b):
    a, b = array(a, dtype=complex), array(b, dtype=complex)
    n = 1
    while n <= a.size or n <= b.size: n <<=1
    n <<= 1
    a.resize(n)
    b.resize(n)

    cs = cos(2*pi/n)
    w = complex(cs, (1-cs*cs)**.5)

    a = fft(a, w)
    b = fft(b, w)
    
    i = 0
    while i < n:
        a[i] *= b[i]
        i += 1
    a = fft(a, w.conjugate())
    return list(map(round, a/n))


if __name__ == '__main__':
    from time import time
    t = time()
    
    N = 10000
    v = mul([1]*N, [1]*N)
    
    print(time()-t)
