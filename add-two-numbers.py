# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getNumber(self, lnklst):
        revlst=[]
        while lnklst is not None:
            revlst.append(lnklst.val)
            lnklst = lnklst.next
        numlst = reversed(revlst)
        return int(''.join(str(digit) for digit in numlst))

    def genLnklst(self, num):
        revlst=reversed(str(num))
        lnklst = None
        for digit in revlst:
            newnode = ListNode(int(digit)) 
            if lnklst is not None:
                lstnode.next = newnode
            else:            
                lnklst = newnode
            lstnode = newnode
        return lnklst

    def getSumLnklst(self, lnklst):
        sumlnklst = []
        while lnklst is not None:
            sumlnklst.append(int(lnklst.val))
            lnklst = lnklst.next
        return sumlnklst

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """     
        num1 = self.getNumber(l1)    
        num2 = self.getNumber(l2)   
        sumnum = num1 + num2     
        sumlnklst = self.genLnklst(sumnum)
        return self.getSumLnklst(sumlnklst)
