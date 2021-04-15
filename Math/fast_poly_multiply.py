'''
O(N logN) Time Complexity
    N     best time
  10000 | 0.015 sec
1000000 | 1.337 sec
9000000 | 20.61 sec
'''

from numpy import array, round, roll, flip
from numpy.fft import fft

def mul(a, b):
    a, b = array(a), array(b)
    n = 1
    while n <= a.size or n <= b.size: n <<=1
    n <<= 1
    a.resize(n)
    b.resize(n)
    
    return flip(roll(round(fft(fft(a)*fft(b))/n), -1))

if __name__ == '__main__':
    from time import time
    t = time()
    
    N = 1000000
    v = mul([1]*N, [1]*N)
    
    print(time()-t)
