'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.
'''

# Use diophantine equation solver from SymPy to solve diophantine (integer) equations.
#
# Manual steps:
#
# 1 - get general solution to x^2 + y^2 = z^2 - returns solution(s) in terms of integers p and q:
#     diophantine(x * x + y * y - z * z)
#     -> set([(2*p*q, p**2 - q**2, p**2 + q**2)])
#
# 2 - sub values for x, y, z (in terms of p & q) into x + y + z = limit to get another diophantine equation:
#     sum([2*p*q, p**2 - q**2, p**2 + q**2])
#     -> 2*p**2 + 2*p*q
# 
# We now have a diophantine equation for the perimeter of a diophantine right triangle - so we get:
# 2 * p * q + 2 * p^2 = limit
# -> p * p + p * q = limit / 2
#
# Automation:
#
# Solve the diophantine equation, and get multiple candidates for p, q.
# For each one, substitute back in to get x, y, z.  In all cases, x * x + y * y = z * z; and x + y + z = limit
# so we need to find out which solutions actually form a real triangle: (x, y, z) all > 0

from sympy.solvers.diophantine import diophantine
from sympy import symbols
            
def main_body(limit):
    p, q = symbols('p q', integer = True)
    return [x * y * z for x, y, z in ((2 * a * b, a * a - b * b, a * a + b * b) for a, b in diophantine(p * p + q * p - limit / 2)) if x > 0 and y > 0][0]
    
def time_test(limit, count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body(' + str(limit) + ')', setup = 'from __main__ import main_body', number = count) / count * 1000) + ' ms'

if __name__ == '__main__':
    assert main_body(12) == 60
    
    limit = 1000
    print time_test(limit, 300)
    result = main_body(limit)
    print result
    
    assert result == 31875000