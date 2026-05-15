class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1) , len(nums2) 
        l, r = 0, n

        while l <= r:
            i = (l + r) // 2 # cantidad de elementos que tomo de nums1
            j = ((m+n+1)) // 2 -i #cantidad elem que tomo de nums2
            nums1_left = nums1[i-1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < n else float('inf')
            nums2_left= nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < m else float('inf')
            if (nums1_left<= nums2_right and nums2_left <=  nums1_right):
                #particion valida
                left_extreme= max(nums1_left, nums2_left)
                right_extreme = min(nums1_right, nums2_right)
                average =(right_extreme + left_extreme ) / 2
                return left_extreme if (n+m) % 2 != 0 else average
            elif  nums1_left > nums2_right:
                r = i -1
            elif nums2_left > nums1_right:
                l = i + 1