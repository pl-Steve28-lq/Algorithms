binarySearchOneline=lambda n,l,t=0:None if not n in l else binarySearchOneline(n,l[len(l)//2:],t+len(l)//2)if l[len(l)//2]<n else binarySearchOneline(n,l[:len(l)//2],t)if l[len(l)//2]>n else t+len(l)//2

def binarySearchBeautify(n, l, t=0):
    a = len(l)//2
    if not n in l: return None
    if l[a]<n: return binarySearchBeautify(n,l[a:],t+a)
    elif l[a]>n: return binarySearchBeautify(n,l[:a],t)
    else: return t+a
