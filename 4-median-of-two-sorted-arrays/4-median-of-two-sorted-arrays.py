class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        concat_nums = nums1 + nums2
        
        mid = len(concat_nums)/2
        heap_top_k = heapq.nsmallest(mid+1, concat_nums)
        
        if len(concat_nums)%2 == 0:
            return (heap_top_k[-1]+heap_top_k[-2])/2.0 #mean of mid and mid+1 elements
        else:
            return heap_top_k[-1] #mid element