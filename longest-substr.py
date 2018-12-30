# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        """

        lst = []
        seq = 0

        for i in s:
            if i in lst:
                lst = lst[lst.index(i)+1::]
                lst.append(i)
            else:
                lst.append(i)
                if len(lst) > seq:
                    seq = len(lst)

        return seq
