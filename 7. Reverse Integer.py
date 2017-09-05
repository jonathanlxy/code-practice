'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Equivalent to cmp(a, b) but compatible with Python 3
        sign = (x > 0) - (x < 0)
        try: # This exception handler is not necessary, but makes
             # the comparison run faster in Python 2
            rev = int(repr(sign * x)[::-1])
            if rev < 2**31: # Max 32-bit = 2**31 - 1
                return sign * rev
            return 0
        except:
            return 0

# Test
a = Solution()
x = [0, 233, -233, 2 ** 31]
for i in x:
  print('reverse {}: {}'.format(i, a.reverse(i)))
