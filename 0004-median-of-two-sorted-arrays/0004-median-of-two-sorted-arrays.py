class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       nums1.extend(nums2)
       print(nums1)
       nums1.sort()
       n=len(nums1)
       if n%2==1:
        return nums1[n//2]
       else:
        mid=n//2
        return (nums1[mid-1]+nums1[mid])/2.0
          
        
        