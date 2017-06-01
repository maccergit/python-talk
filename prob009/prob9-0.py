'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.
'''
            
def main_body(limit):
    # Since a < b < c, the smallest c can be is 1/3 of the total.
    # Likewise, the largest it can be is 1/2 of the total (as a approaches 0, b and c approach each other in a triangle)
    for c in xrange(limit / 3, limit / 2 + 1) :
        max_blimit = limit - c - 1
        if max_blimit >= c :
            max_blimit = c - 1
        min_blimit = max_blimit / 2
        for b in xrange(min_blimit, max_blimit + 1) :
            a = limit - c - b
            if a < b :
                if a * a + b * b == c * c :
                    return a * b * c
    
def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000) + ' ms'

if __name__ == '__main__':
    assert main_body(12) == 60
    
    limit = 1000
    print time_test(limit)
    result = main_body(limit)
    print result
    
    assert result == 31875000