'''
Useful functions - used multiple times, so factored to a module.
'''

# consider trying these with SymPy replacements - might be faster
# also - consider doing some of the projects with SymPy replacements (it does Diophantine solutions, for example)

def alphaValue(name):
    return sum(ord(letter) - 64 for letter in name)

def prod(iterableArg):
    import operator
    return reduce(operator.mul, iterableArg)

def primeGeneratorFunction():
    yield 2
    primes = set() # Since we don't bother with even values, we don't need 2 in the primes list
    current = 3
    
    while True:
        for divisor in primes:
            if current % divisor == 0:
                current += 2 # don't bother with even values
                break
        else:
            primes.add(current)
            yield current

def primes(limit):
    from collections import deque
    nums = deque([x for x in xrange(2, limit)])
    primes = deque([])
    while nums and nums[0] * nums[0] < limit :
        prime = nums.popleft()
        primes.append(prime)
        nums = deque([x for x in nums if x % prime != 0])
    primes.extend(nums)
    return primes

def firstFactor(n):
    for candidate in primeGeneratorFunction() :
        if candidate * candidate <= n:
            if n % candidate == 0:
                return candidate
        else:
            return n

def factor(n):
    retval = [firstFactor(n)]
    
    while retval[-1] != n:
        n /= retval[-1]
        retval.append(firstFactor(n))
        
    return retval