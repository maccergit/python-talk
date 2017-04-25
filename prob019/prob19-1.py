# coding: utf-8

'''
You are given the following information, but you may prefer to do some research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import datetime

def main_body():
    return sum(1 for mm in xrange(1, 13) for yyyy in xrange(1901, 2001) if datetime.datetime(yyyy, mm, 1).weekday() == 6)
    
def time_test(count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body()', setup = 'from __main__ import main_body', number = count) / count * 1000000) + ' µs'

if __name__ == '__main__':
    
    print time_test(10000)
    result = main_body()
    print result
    
    assert result == 171