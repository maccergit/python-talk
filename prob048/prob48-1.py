# coding: utf-8

'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

def main_body(limit):
    return sum(x ** x for x in xrange(1, limit + 1)) % 10000000000
    
def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000) + ' ms'

if __name__ == '__main__':
    
    assert main_body(10) == 405071317
    
    limit = 1000
    print time_test(limit)
    result = main_body(limit)
    print result
    
    assert result == 9110846700