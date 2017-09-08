# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def com_index_finder(self, str1, str2):
        i = 0
        while i < min(len(str1), len(str2)):
            if str1[i] == str2[i]:
                i += 1
            else:
                break
        return str1[:i]
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs):
            com = reduce(self.com_index_finder, strs)
            return com
        return ''

# A slower but more elegant solution:
'''
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            print i, letter_group, set(letter_group)
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
'''
a = Solution()
strs = ['mr1', 'mrs2', 'mrstr3']
print a.longestCommonPrefix(strs)
