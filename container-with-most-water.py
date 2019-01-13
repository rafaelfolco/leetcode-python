# https://leetcode.com/problems/container-with-most-water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        """
        c_maxwater = 0
        size=len(height)

        start = 0
        end = size - 1

        for i in xrange(size):
            c_height = min(height[start], height[end])
            c_width = end - start
            c_area = c_height * c_width
            c_maxwater = max(c_maxwater, c_area)

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return c_maxwater
