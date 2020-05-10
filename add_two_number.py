# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: listNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = None
        a = 0
        while l1 or l2 or a:
            if l1:
                a += l1.val
                l1 = l1.next
            if l2:
                a += l2.val
                l2 = l2.next
            if l3:
                l3.next = ListNode(a%10)
                l3 = l3.next
            else:
                l4 = ListNode(a%10)
                l3 =l4
            a = a//10
        return l4
