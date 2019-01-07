#https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode


        node = head
        length = 0

        while node is not None:
            length += 1
            node = node.next

        node = head
        if length > 1 and n < length:
            nth = length - n
            for i in range(1, nth):
                node = node.next
            n_node = node.next
            if n_node.next is not None:
                following_node = n_node.next
                node.next = following_node
            else:
                node.next = None
        else:
            head = head.next

        return head

        """

        ref = nth = head

        for _ in range(n):
            ref = ref.next

        if not ref:
            return head.next

        while ref.next:
            ref = ref.next
            nth = nth.next

        nth.next = nth.next.next

        return head

