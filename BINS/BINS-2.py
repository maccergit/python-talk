# coding: utf-8

'''
The problem is to find a given set of keys in a given array.

Given: Two positive integers n≤10^5 and m≤10^5, a sorted array A[1..n] of integers
from −10^5 to 10^5 and a list of m integers −10^5≤k1,k2,…,km≤10^5.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.
'''

# Use a set for a lookup table

def solve(infile, outfile):
    # we don't need the array sizes in python - so skip them
    next(infile)
    next(infile)
    keys = {}
    current = 1
    for x in next(infile).strip().split():
        keys[int(x)] = str(current)
        current += 1
    search = [int(x) for x in next(infile).strip().split()]
    outfile.write(" ".join(keys.get(x, '-1') for x in search))

def main_body(filename):
    with open(filename) as f:
        with open('result.txt', 'w') as out:
            solve(f, out)
    return 'Done'

def time_test(count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body("rosalind_bins.txt")', setup = 'from __main__ import main_body', number = count) / count * 1000) + ' ms'

if __name__ == '__main__':
    print time_test(100)