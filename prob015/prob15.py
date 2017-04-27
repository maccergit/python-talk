# coding: utf-8

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

w/o cache:
12 -> 717 msec
13 -> 2.7 sec
14 -> 10.2 sec
'''

known = {}

def routes(limit, x, y):
    if (x, y) in known:
        return known[(x, y)]
    retval = 0
    if x == limit:
        retval += 1
    if y == limit:
        retval += 1
    if x < limit:
        retval += routes(limit, x + 1, y)
    if y < limit:
        retval += routes(limit, x, y + 1)
    known[(x, y)] = retval
    return retval

def main_body(limit):
    global known
    known = {}
    return routes(limit, 1, 1)
    
def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000000) + ' µs'

if __name__ == '__main__':
    assert main_body(2) == 6
    
    limit = 20
    print time_test(limit, 10000)
    result = main_body(limit)
    print result
    
    assert result == 137846528820