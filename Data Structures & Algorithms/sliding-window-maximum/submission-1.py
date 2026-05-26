class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k :
            return []
        left = 0
        right =k - 1
        res = []
        currMax = 0
        while right < len(nums):
            currMax = max(nums[left: right +1])
            res.append(currMax)
            left += 1
            right +=1
        return res

            