'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

Hint:

If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?
'''

'''
Jonathan Liu
As hinted, if there are 4 stones, the next player will always win. Therefore, as long as you can transform the current number of stones into multiple of 4 and leave it to your opponent, then you are guaranteed to win (no matter how many stones removed by your opponent, just take the number of stones that can make the rest as multiple of 4 again). 
'''

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0

# Test
a = Solution()
a.canWinNim(4)
a.canWinNim(5)