class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatest = 0

        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            greatest = max(greatest, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return greatest
