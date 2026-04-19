class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l= 0
        r = n-1
        maxL = 0
        maxR = 0
        maxA= 0
        while l <= r: 
            iArea= 0
            if maxL <= maxR:
                maxL = max(maxL, height[l])
                iArea= maxL - height[l]
                l+=1
            else:
                maxR= max(maxR, height[r])
                iArea = maxR - height[r]
                r-=1
            maxA += iArea
        return maxA


            

        