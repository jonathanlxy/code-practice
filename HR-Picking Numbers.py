'''
Picking Numbers
Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is .
Example 1: 
  Input = '4 6 5 3 3 1', the matching collection is (4, 3, 3), 
  Thus the return value should be the length of this collection: 3
Example 2:
  Input: 1 2 2 3 1 2
  Output = 5 (length of 1, 2, 2, 1, 2)
'''

from collections import Counter
from datetime import datetime

def timer(func):
    def f(*args, **kwargs):
        now = datetime.now()
        rv = func(*args, **kwargs)
        print datetime.now() - now
        return rv
    return f

@timer
def func1(a):
    hashed = Counter(a)
    if len(hashed) > 1:
        sorted_hash = sorted(hashed.items(), reverse = True)
        paired_sum = []
        p0, p1 = 0, 1
        while p1 < len(sorted_hash):
            if sorted_hash[p0][0] - sorted_hash[p1][0] == 1:
                paired_sum.append(
                (sorted_hash[p0][0] + sorted_hash[p1][0],
                sorted_hash[p0][1] + sorted_hash[p1][1]))
            p0 += 1
            p1 += 1
        sum_max = sorted(paired_sum, key = lambda x: x[1], reverse = True)[0][1]
        hash_max = max(hashed.values())
        if hash_max < sum_max:
            return sum_max
        return hash_max
    return hashed.items()[0][1]

@timer
def func2(a):
    return max(a.count(i) + a.count(i - 1) for i in set(a))

# Test it
i = '66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66'
a = map(int, i.strip().split(' '))

print func1(a)
print func2(a)
