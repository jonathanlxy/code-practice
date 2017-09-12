'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_par = {'(': ')',
                    '{': '}',
                    '[': ']'}
        stack = []
        # Before traverse, judge based on meta feature
        if (not len(s)) or (len(s) % 2) or (s[0] not in left_par):
            return False
        for l in s:
            # Push
            if l in left_par:
                stack.append(l)
            # Pop & match
            elif left_par[stack.pop()] != l:
                return False
        # If traverse finished without item left in stack, it's a valid string
        if len(stack):
            return False
        return True


s1 = ''
s2 = '[]'
s3 = '[{)}]'
s4 = '[{]}'
s5 = '({[]})'
s6 = '(('

a = Solution()
print a.isValid(s1) # F
print a.isValid(s2) # T
print a.isValid(s3) # F
print a.isValid(s4) # F
print a.isValid(s5) # T
print a.isValid(s6) # F
