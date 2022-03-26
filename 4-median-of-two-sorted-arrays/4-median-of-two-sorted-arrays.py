class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1)+len(nums2)
        
        i, j = None, None
        if total%2 == 0:
            i = total/2
            j = i+1
            l = heapq.nsmallest(j, nums1+nums2)
            return (l[-1]+l[-2])/2.0 #mean of mid and mid+1 elements
        else:
            i = total/2
            j = i+1
            l = heapq.nsmallest(j, nums1+nums2)
            return l[-1] #mid element