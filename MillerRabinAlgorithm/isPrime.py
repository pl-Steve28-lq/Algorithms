from random import randint

def gcd(m,n):
	rem = 0
	while n > 0:
		rem = m%n
		m = n
		n = rem
	return m

def fastExp(m,e,n):
	z = 1
	while e>0:
		while not e%2:
			e = e//2
			m = (m*m)%n
		e -= 1
		z = (z*m)%n
	return z

def isPrime(n):
	m = n-1
	k = 0
	while not m%2:
		m = m//2
		k += 1
	for i in range(100):
		f = randint(2,n-1)
		a = f*(n-2) if n>2 else 2
		if gcd(a,n) != 1: return False
		b = fastExp(a,m,n)
		if b == 1 or b == (n-1): continue
		else:
			for j in range(k-1):
				b = (b*b)%n
				if b == n-1: break
			if b != n-1: return False
	return True
