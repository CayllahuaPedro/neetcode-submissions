class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        def buildSubSets(i: int, numList:List):
            if i > len(nums):
                return
            if i ==len(nums):
                res.append(numList)
                return
            num = nums[i]
            include = [*numList, num]
            buildSubSets(i+1, include)
            buildSubSets(i+1, numList)
        included = []
        buildSubSets(0, included)
        return res  
        