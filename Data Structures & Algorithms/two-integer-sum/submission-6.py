class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {} # osea seria {num: index}
        for i in range(n):
            current = nums[i]
            diff = target - current
            if diff in seen: 
                return [seen[diff], i]
            else:
                seen[current] = i