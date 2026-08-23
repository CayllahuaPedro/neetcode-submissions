class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def findComb(i:int, sum: int, curr:List[int]):
            if sum == target:
                res.append([*curr])
                return
            for j in range(i, n):
                newSum = sum + nums[j]
                if newSum > target:
                    continue
                else:
                    newCurr = [*curr, nums[j]]
                    findComb(j,sum+nums[j], newCurr)
            return
        findComb(0, 0, [])             
        return res