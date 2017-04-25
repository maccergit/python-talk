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

month_days = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

month_julian = { mm : sum(month_days[index] for index in xrange(1, mm + 1)) for mm in xrange(1, 13)}

def leap_year(yyyy):
    if yyyy % 4 == 0:
        if yyyy % 100 == 0:
            if yyyy % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

def compute_days(yyyy, mm):
    if mm == 0:
        return 0
    if mm > 1:
        return month_julian[mm] + leap_year(yyyy)
    return month_julian[mm]

def main_body():
    mm_julian = {yyyy : {mm : compute_days(yyyy, mm) for mm in xrange(0, 13)} for yyyy in xrange(1901, 2001)}
    yyyy_julian = {1900 : 0}
    
    for yyyy in xrange(1901, 2001):
        yyyy_julian[yyyy] = 365 + leap_year(yyyy) + yyyy_julian[yyyy - 1]
    
    count = 0
    
    for yyyy in xrange(1901, 2001):
        for mm in xrange(1, 13):
            julian = yyyy_julian[yyyy - 1] + mm_julian[yyyy][mm - 1]
            if (julian + 2) % 7 == 0:
                count += 1
    return count
    
def time_test(count = 1000):
    import timeit
    return str(timeit.timeit(stmt = 'main_body()', setup = 'from __main__ import main_body', number = count) / count * 1000000) + ' µs'

if __name__ == '__main__':
    
    print time_test(10000)
    result = main_body()
    print result
    
    assert result == 171