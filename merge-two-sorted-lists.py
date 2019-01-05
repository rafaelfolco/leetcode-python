# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        """
        merged_list = []
        while l1 != None or l2 != None:
            if l1 != None:
                merged_list.append(l1.val)
                l1 = l1.next
            if l2 != None:
                merged_list.append(l2.val)
                l2 = l2.next

        lnk_merged_list = None
        for i in sorted(merged_list):
            new = ListNode(i)
            if lnk_merged_list == None:
                lnk_merged_list = new
            else:
                last.next = new
            last = new
        return lnk_merged_list
