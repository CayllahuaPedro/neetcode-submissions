from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        dq = deque()
        left = 0
        res =[]
        for right in range(len(nums)):
            while len(dq) > 0 and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)
          
            if right - left + 1 > k:
                # tengo que actualizar left
                if left >= dq[0]:
                    dq.popleft()
                left += 1
            if right - left + 1 == k:
                res.append(nums[dq[0]])
        return res