class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize lists with 1s so indices exist
        prefix_prod = [1] * n
        sufix_prod = [1] * n
        
        # Calculate Prefix Products
        acc = 1
        for i in range(n):
            prefix_prod[i] = acc
            acc *= nums[i]
            
        # Calculate Suffix Products
        acc = 1
        for i in range(n - 1, -1, -1):
            sufix_prod[i] = acc
            acc *= nums[i]
        
        # Your zip logic works perfectly here!
        return [p * s for p, s in zip(prefix_prod, sufix_prod)]