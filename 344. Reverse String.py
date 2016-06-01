'''
Write a function that takes a string as input and returns the string reversed.
'''

'''
Jonathan Liu
This is a no-brainer for python users...
'''

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

a = Solution()
print a('Hello')