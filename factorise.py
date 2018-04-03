import math

def factorise(n):
    while ( n%2 == 0 ):
        yield 2
        n = n//2
    while ( n%3 == 0 ):
        yield 3
        n = n//3
    lf = 6
    while True:
        f = False
        for d in range(lf, int(math.sqrt(n)+1), 6):
            if n%(d+1) == 0:
                yield d+1
                n = n/(d+1)
                lf = d
                f = True
                break
            if n%(d-1) == 0:
                yield d-1
                n = n/(d-1)
                lf = d
                f = True
                break
        if not f:
            yield int(n)
            break
        
print(list(factorise(1234524321)))
print(list(factorise(207519531250)))
print(set(factorise(207519531250)))
