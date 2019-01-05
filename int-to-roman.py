# https://leetcode.com/problems/integer-to-roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        one = {'unit':'I', 'five':'V'}    
        ten = {'unit':'X', 'five':'L'}
        hundred = {'unit':'C', 'five':'D'}
        thousand = {'unit':'M'}

        roman = {
            3: one,
            2: ten,
            1: hundred,
            0: thousand
        }

        roman_str = "" 
        str_num = "%04d" % num

        for x in xrange(len(str_num)-1, -1, -1):
            roman_class = roman.get(x)
            n = int(str_num[x])
            if n >= 1 and n <= 3:
                for i in range(1, n+1):
                    roman_str += roman_class.get('unit')
            elif n == 4:
                roman_str += roman_class.get('five')
                roman_str += roman_class.get('unit')
            elif n == 5:
                roman_str += roman_class.get('five')
            elif n >=6 and n <=8:
                for i in range(1, -4+n):
                    roman_str += roman_class.get('unit')
                roman_str += roman_class.get('five')
            elif n == 9:
                roman_class_next = roman.get(x-1)
                roman_str += roman_class_next.get('unit')
                roman_str += roman_class.get('unit')

        return roman_str[::-1]
