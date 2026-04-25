class Solution:
    def recuSearch(self, array: List[int], li : int, hi : int, target: int) -> int:
        middle : int = (li + hi) // 2
        
        if  hi < li: 
            return -1
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            return self.recuSearch(array,middle +1 , hi,target)
        else: 
            return self.recuSearch(array,li, middle -1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.recuSearch(nums , 0, len(nums) -1,target)