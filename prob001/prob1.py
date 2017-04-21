# coding: utf-8

'''
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def main_body(limit):
    return sum(x for x in xrange(limit) if x % 3 == 0 or x % 5 == 0)

def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000000) + ' µs'

if __name__ == '__main__':
    assert main_body(10) == 23
    
    limit = 1000
    print time_test(limit, 100000)
    result = main_body(limit)
    print result
    
    assert result == 233168