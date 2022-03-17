import numba
from numba import jit

def primes():
    filename = "primes.txt" # Thanks to https://primes.utm.edu/ for the primes
    lines=[]
    with open(filename) as diary_file:
        n = 1
        for line in diary_file:
            lines.append(line)

    return lines

lines = primes()
primenos = []
for line in lines:
    nos=line.split('    ')
    for num in nos:
        # print(num.split(' '))
        for x in num.split(' '):
            if x.strip().isnumeric():
                primenos.append(int(x.strip()))
gaps=[];
i=0;
for x in primenos:
    i+=1;
    if(i==len(primenos)):
        break;
    # print()
    gaps.append(primenos[i]-primenos[i-1])    
print(gaps)
