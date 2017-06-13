# coding: utf-8

'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...
             ^

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''


# Jython specific - sStringBuffer works better than Python String, but is Java class

import tools.tools as t
import java

def main_body(limit):
    value_buffer = java.lang.StringBuffer('0.')
    for x in xrange(1, 10 ** limit):
        value_buffer.append(x)
    value_string = str(value_buffer)
    return t.prod(int(value_string[1 + 10 ** x]) for x in xrange(0, limit + 1))
    
def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000) + ' ms'

if __name__ == '__main__':
    
    limit = 6
    print time_test(limit, 1)
    result = main_body(limit)
    print result
    
    assert result == 210