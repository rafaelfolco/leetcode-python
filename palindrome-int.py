# https://leetcode.com/problems/palindrome-number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_x = str(x)
        pal=False

        if str_x == str_x[::-1]:
            pal=True

        return pal
