# https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = sorted(nums1 + nums2)
        nlen = len(nums)
        half = abs(nlen / 2)
        if nlen % 2 == 0:
            median = (nums[half]+nums[half-1])/2.0
        else:
            median = nums[half]

        return median
