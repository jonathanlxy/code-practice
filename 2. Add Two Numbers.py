'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Result list and a dummy pointer
        result = ListNode(0)
        node = result
        # Pointers for loop
        p1, p2 = l1, l2
        # Carry over
        carry = 0
        # Visit through lists, add digits and append to next node
        while p1 or p2:
            if not p1:
                _sum = p2.val
                p2 = p2.next
            elif not p2:
                _sum = p1.val
                p1 = p1.next
            else:
                _sum = p1.val + p2.val
                p1, p2 = p1.next, p2.next
            _sum += carry
            # Store carry to temp slot
            carry = _sum // 10
            node.next = ListNode(_sum % 10)
            node = node.next
        # After looped through the list, if still remaining carry value, append
        if carry:
            node.next = ListNode(carry)
        return result.next
