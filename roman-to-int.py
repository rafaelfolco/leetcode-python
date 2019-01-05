# https://leetcode.com/problems/roman-to-integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        III 1+1+1
        IV  +4
        CD  +400

        """

        roman = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000,
        }

        num=0
        i = len(s)-1
        while i >= 0:
            n=None
            symbol = s[i]
            if i > 0:
                prev_symbol = s[i-1]
                n = roman.get(prev_symbol+symbol)

            #handle 4s and 9s
            if n is not None:
                num += n
                i -= 1
            else:
                num += roman.get(symbol)

            i -= 1

        return num
