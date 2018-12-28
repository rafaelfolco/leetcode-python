# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        input:
                nums=[2.7.11.15]
                target=9

        # O(n2) solution --> runtime: 28 ms

           = 2
          /
        idx1 > one-by-one 
        [2, 3, 6, 4, 9]
            idx2
               \
                = 3
        # use enumerate to access indices

        for idx1, val1 in enumerate(nums):
            for idx2, val2 in enumerate(nums[idx1+1::], start=idx1+1):
                if val1 + val2 == target:
                    return idx1, idx2

        # O(n) solution  --> runtime: 20 ms
        test:

        target=9
        aux={} >> {2:0}
        idx=0 >> 1
        val=2 >> 7 
        diff=9 >> 2

        return=[0,1]
        """

        aux = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in aux:
                return aux.get(diff), idx
            aux[val] = idx
