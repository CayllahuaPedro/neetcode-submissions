class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        found = -1
        while left<= right:
            middle = (right + left ) //2
            if target == nums[middle]:
                found = middle
                break
            if nums[left] < nums[middle]:
                #esta ordeando a al izq, voy por alla
                if nums[left]<= target <  nums[middle]:
                    right = middle -1
                else:
                    left = middle +1
            elif nums[middle] < nums[right]:
                if nums[middle] < target <= nums[right]:
                    left = middle +1 
                else:
                    right = middle -1
            else:
                left+=1
        return found
        