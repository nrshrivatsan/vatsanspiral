#Thanks to http://users.softlab.ece.ntua.gr/~ttsiod/primes.html
import math
import itertools

#Thanks to http://users.softlab.ece.ntua.gr/~ttsiod/primes.html
#Generates Primes
def _primes():
    yield 2
    primesSoFar = [2]
    for candidate in itertools.count(3, 2):
        for prime in (i for i in primesSoFar if i <= int(math.sqrt(candidate))):
            if 0 == candidate % prime:
                break
        else:
            primesSoFar.append(candidate)
            yield candidate

def main():    
    pz = []
    for p in _primes():
        if p > 151:
            break
        # print p,
        pz.append(p)
    
    return pz

if __name__ == "__main__":
    print main()