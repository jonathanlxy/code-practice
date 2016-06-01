'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''

'''
Jonathan Liu
'''

'''
# Approach 1: recursive adding

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        add_up = sum(map(int, list(str(num))))
        if add_up >= 10:
            return self.addDigits(add_up)
        return add_up
'''

# Approach 2: Digital root
# https://en.wikipedia.org/wiki/Digital_root

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
        	return 0
        else:
        	if num % 9 == 0:
        		return 9
        	else:
        		return num % 9

# Test
a = Solution()
print a.addDigits(10)
print a.addDigits(657)