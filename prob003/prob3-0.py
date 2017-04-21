'''
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

import tools.tools as t

def main_body(limit):
    return max(t.factor(limit))
    
def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000) + ' ms'

if __name__ == '__main__':
    assert main_body(13195) == 29
    
    limit = 600851475143
    print time_test(limit)
    result = main_body(limit)
    print result
    
    assert result == 6857