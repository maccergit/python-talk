'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from sympy import prime
            
def main_body(limit):
    return prime(limit)

def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000) + ' ms'

if __name__ == '__main__':
    assert main_body(6) == 13
    
    limit = 10001
    print time_test(limit, 100)
    result = main_body(limit)
    print result
    
    assert result == 104743