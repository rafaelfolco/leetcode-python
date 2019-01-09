# https://leetcode.com/problems/zigzag-conversion

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str

        """

        if numRows == 1:
            return s

        rows = [''] * numRows
        i = 0
        down = True

        for l in s:
            rows[i] += l
            if down:
                i += 1
                if i == numRows-1:
                    down = False
            else:
                i -= 1
                if i == 0:
                    down = True 

        _str = ''
        for i in range(numRows):
            _str += rows[i]

        return _str
