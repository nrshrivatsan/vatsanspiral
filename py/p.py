#https://github.com/spmacdonald/ulam_spiral/blob/master/ulam.py
from math import sqrt
import math
import itertools

#Thanks to  http://stackoverflow.com/a/2659378/2917986
import numpy as np
import scipy.misc
import sys


#Thanks to http://users.softlab.ece.ntua.gr/~ttsiod/primes.html
#Generates Primes
primeNumbers = []

dimension = 1901

upperBound = 500000

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

def get_all_primes():    
    global upperBound
    pz = []
    for p in _primes():
        if p > upperBound:
            break
        # print p,
        pz.append(p)
    return pz       

def ulam_spiral(grid_size):
    global primeNumbers
    grid = init_spiral(grid_size)
    coords = generate_coords(grid_size+2)

    # Fill the grid with the increasing integers spiraling outwards from the
    # center.
    for i, c in enumerate(coords):
        x = c[0] + (grid_size // 2)
        y = c[1] + (grid_size // 2)
        if i in primeNumbers:
            grid[y][x] = 1
        else:
            grid[y][x] = 0
    return grid

def generate_coords(grid_size):
    """ Compute the cartesian (x, y) coordinates for the Ulam spiral entries.
    grid_size must be odd. """
    x_coords = [[0]]
    y_coords = [[0]]
    for i, n in enumerate(xrange(3, grid_size, 2)):
        seq1 = [n-(2+i) for x in xrange(n)]
        seq2 = [x-(i+1) for x in reversed(xrange(n))]
        seq3 = [(2+i)-n for x in xrange(n)]
        seq4 = [x-(i+1) for x in xrange(n)]
        x_coords.append(seq1[1:] + seq2[1:] + seq3[1:] + seq4[1:])
        y_coords.append(seq4[1:] + seq1[1:] + seq2[1:] + seq3[1:])

    x_coords = list(from_iterable(x_coords))
    y_coords = list(from_iterable(y_coords))
    coords = zip(x_coords, y_coords)
    return coords

def init_spiral(grid_size):
    """ Initialize a grid with all zeros. """
    return [[0 for i in range(grid_size)] for j in range(grid_size)]

def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
            
def print_grid(grid):
    """ Pretty print the grid with the proper spacing. """
    max_element = max(map(max, grid))
    num_digits = len(str(max_element))
    for row in grid:
        row = map(lambda x: str(x).rjust(num_digits, ' '), row)
        print ' '.join(row)

def factors(n):
    """ Compute the factors of n. """
    if n == 0: return set()
    return set(reduce(list.__add__, ([i, n/i] for i in xrange(1, int(sqrt(n) + 1)) if n % i == 0)))

def test():
    global primeNumbers
    global dimension
    primeNumbers = get_all_primes()
    # print "Numbers Generated til",str( primeNumbers[ ( len(primeNumbers)-1 ) ] )
    grid = ulam_spiral(dimension)
    scipy.misc.imsave('./'+str(dimension)+'.png', grid)
    # print_grid(grid)

if __name__ == '__main__':
    test()