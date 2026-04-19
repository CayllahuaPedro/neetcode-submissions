class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left =0
        right=n-1
        maxArea= 0

        while left< right: 
            currArea= (right-left) * min(heights[left], heights[right])
            maxArea = max(maxArea, currArea)
            if (heights[left] < heights[right]):
                left+=1
                continue
            if (heights[right] < heights[left]):
                right-=1 
                continue
            if heights[left+1]:
                diff = heights[left] - heights[left+1]
                if diff < 0:
                    left +=1
                    continue
                else:
                    right -=1
                    continue
            else: 
                right-=1
                continue

            if heights[right-1]:
                diff = heights[right] - heights[right-1]
                if diff < 0:
                    right-=1
                    continue
                else: 
                    left+=1
                    continue
            else: 
                left+=1
                continue


        return maxArea