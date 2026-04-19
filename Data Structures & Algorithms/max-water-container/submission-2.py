class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            curr_area = width * min(heights[left], heights[right])
            max_area = max(max_area, curr_area)
            
            # Always move the pointer pointing to the shorter height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area