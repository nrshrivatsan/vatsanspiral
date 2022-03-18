import numba
from numba import jit

def primes():
    ''' Reads the prime numbers file and returns an array of integers
    '''
    filename = "primes.txt" # Thanks to https://primes.utm.edu/ for the primes
    lines=[]
    with open(filename) as diary_file:
        n = 1
        for line in diary_file:
            lines.append(line)
    return lines

def divby2(gaps):
    '''Divides the given raw-gaps input and returns a divided by two value '''
    divby2=[]
    for gap in gaps:
        divby2.append(int(gap/2))
    return(divby2);

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
divby2=divby2(gaps)
# print(divby2[0:int(len(divby2)/2)]);


#https://www.geeksforgeeks.org/how-to-count-the-frequency-of-unique-values-in-numpy-array/#:~:text=Python%E2%80%99s%20numpy%20library%20provides%20a%20numpy.unique%20%28%29%20function,array%20with%20their%20corresponding%20frequency%20counts%20NumPy%20array.?msclkid=c5b0c0aba65011ecbeae60657079bb5c
import numpy as np
  
# Get a tuple of unique values 
# and their frequency in
# numpy array
unique, frequency = np.unique(np.array(divby2), 
                              return_counts = True)
# print unique values array
print("Unique Values:", unique)
# print frequency array
print("Frequency Values:",
      frequency)


# import numpy as np
# def find_runs(x):
#     # https://stackoverflow.com/a/58540073
#     """Find runs of consecutive items in an array."""
#     # ensure array
#     x = np.asanyarray(x)
#     if x.ndim != 1:
#         raise ValueError('only 1D array supported')
#     n = x.shape[0]

#     # handle empty array
#     if n == 0:
#         return np.array([]), np.array([]), np.array([])

#     else:
#         # find run starts
#         loc_run_start = np.empty(n, dtype=bool)
#         loc_run_start[0] = True
#         np.not_equal(x[:-1], x[1:], out=loc_run_start[1:])
#         run_starts = np.nonzero(loc_run_start)[0]

#         # find run values
#         run_values = x[loc_run_start]

#         # find run lengths
#         run_lengths = np.diff(np.append(run_starts, n))

#         return run_values, run_starts, run_lengths
# # from itertools import groupby
# # print([(k, sum(1 for i in g)) for k,g in groupby(divby2)])
# run_values, run_starts, run_lengths=find_runs(divby2)
# for x in run_values:
#     print(run_values)
