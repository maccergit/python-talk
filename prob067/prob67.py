# coding: utf-8

'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle
with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether!
If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
'''

def main_body():
    with open('p067_triangle.txt') as src:
        data = [[int(elem) for elem in line.split()] for line in src]
    data.reverse()
    for current in xrange(0, len(data) - 1):
        line = data[current]
        data[current + 1] = [a + b for a , b in zip([max(line[index:index + 2]) for index in xrange(0, len(line) - 1)], data[current + 1])]
    return data.pop()[0]
    
def time_test(count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body()', setup = 'from __main__ import main_body', number = count) / count * 1000) + ' ms'

if __name__ == '__main__':
    
    print time_test()
    result = main_body()
    print result
    
    assert result == 7273