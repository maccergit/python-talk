# coding: utf-8

'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def addLayer(a):
    n = len(a)
    last_value = a[0][n - 1]
    for offset in xrange(1, n + 1):
        a[offset - 1].append(last_value + offset)
        a[n - offset].insert(0, last_value + n * 2 + 2 + offset)
    a.append([x for x in xrange(last_value + n * 2 + 2, last_value + n, -1)])
    a.insert(0, [x for x in xrange(last_value + n * 3 + 3, last_value + n * 4 + 5)])
    return a

def compute(a):
    n = len(a)
    return(sum(a[x][x] for x in xrange(0, n)) + sum(a[n - x - 1][x] for x in xrange(0, n)) - 1)

def main_body(limit):
    a = [[1]]
    for x in xrange(0, limit / 2):
        a = addLayer(a)
    return compute(a)
    
def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000) + ' ms'

if __name__ == '__main__':
    
    assert main_body(5) == 101
    
    limit = 1001
    print time_test(limit, 10)
    result = main_body(limit)
    print result
    
    assert result == 669171001