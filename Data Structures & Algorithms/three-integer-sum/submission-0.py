class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        left = 0
        right = n-1
        triplets=[]
        nums.sort()

        for i in range (0, n-2): 
            left = i+1 
            right = n-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right: 
                total = nums[i] + nums[left] + nums[right]
        
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Found a triplet
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return triplets