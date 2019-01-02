# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        rev=120 >> r=021
        rev=-763 >> r=-367
        rev>()2**31)-1 >> r=0 

        """

        max = (2**31)-1
        min = -2**31

        str_num = str(x)

        if str_num[0] == '-':
            rev_num = int(str_num[:0:-1])
            rev_num = rev_num * -1 
        else:
            rev_num = int(str_num[::-1])

        if rev_num < min or rev_num > max:
            return 0    

        return rev_num
