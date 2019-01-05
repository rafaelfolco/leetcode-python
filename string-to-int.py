# https://leetcode.com/problems/string-to-integer-atoi

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if len(str)==0:
            return 0

        signal=0
        num_str = ""
        numbers = ['0','1','2','3','4','5','6','7','8','9']

        maxint = 2**31

        first_is_number=False

        for c in str:
            if c in numbers:
                if signal == 0:
                    signal = 1
                first_is_number=True
                num_str += c
            elif c == '-':
                if signal == 0:
                    signal = -1
                elif len(num_str) > 0:
                    # ignore signal after number
                    break
                else:
                    #can't have two signals
                    return 0
            elif c == '+':
                if signal == 0:
                    signal = 1
                elif len(num_str) > 0:
                    # ignore signal after number
                    break
                else:
                    #can't have two signals
                    return 0
            elif c == ' ':
                if first_is_number or signal != 0:
                    #conversion stops here
                    break
            elif c != ' ':
                if first_is_number:
                    #conversion stops here
                    break
                else:
                    #first is not number, can't
                    return 0

        if len(num_str) == 0:
            return 0

        conv_int = int(num_str) * signal

        if conv_int > 0:
            if conv_int > maxint-1:
                conv_int = maxint-1
        elif conv_int < 0:
            maxint *= signal
            if conv_int < maxint:
                conv_int = maxint

        return conv_int
