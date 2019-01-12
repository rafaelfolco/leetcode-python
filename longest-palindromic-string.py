# https://leetcode.com/problems/longest-palindromic-substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        slen=len(s)
        if slen > 1000:
            return ""
        elif slen == 1:
            return s

        longest = ""
        lsize=0

        for i in xrange(slen):
            if lsize > (slen-i):
                break
            for j in xrange(slen, i, -1):
                if lsize > (j-i):
                    break
                substr = s[i:j]
                if substr == substr[::-1]:
                    longest = substr
                    lsize = len(longest)
                    break

        return longest
