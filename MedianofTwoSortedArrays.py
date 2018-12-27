class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mergelist = sorted(nums1 + nums2)
    
        n = len(mergelist)//2

        if len(mergelist) % 2 == 0:
            return (mergelist[n] + mergelist[n-1]) / 2
        else:
            return mergelist[n]
