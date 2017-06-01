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

# NumPy - cannot use Jython or PyPy - CPython only (and is slower than original design, because it's not a good use of NumPy)

import numpy

def addLayer(a, x):
    current_x = current_y = len(a) / 2 + x
    current = a[current_x, current_y] + 1
    current_x += 1
    for index in xrange(0, 2 * x + 1):
        a[current_x, current_y] = current
        current_y -= 1
        current += 1
    for index in xrange(0, 2 * x + 2):
        a[current_x, current_y] = current
        current_x -= 1
        current += 1
    for index in xrange(0, 2 * x + 2):
        a[current_x, current_y] = current
        current_y += 1
        current += 1
    for index in xrange(0, 2 * x + 3):
        a[current_x, current_y] = current
        current_x += 1
        current += 1

def compute(a):
    n = len(a)
    return numpy.trace(a) + numpy.trace(numpy.flipud(a)) - 1

def main_body(limit):
    a = numpy.empty((limit, limit), int)
    a[limit / 2, limit / 2] = 1
    for x in xrange(0, limit / 2):
        addLayer(a, x)
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