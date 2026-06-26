class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tor, hare= 0,0
        while True:
            tor = nums[tor]
            hare = nums[nums[hare]]
            if tor == hare:
                break
        tor2 = 0
        while True:
            tor = nums[tor]
            tor2 = nums[tor2]
            if tor == tor2:
                break
        return tor