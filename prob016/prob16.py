# coding: utf-8

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def main_body(limit):
    return sum(int(x) for x in str(2 ** limit))
    
def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000000) + ' µs'

if __name__ == '__main__':
    assert main_body(15) == 26
    
    limit = 1000
    print time_test(limit, 100000)
    result = main_body(limit)
    print result
    
    assert result == 1366