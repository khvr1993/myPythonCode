from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        https://leetcode.com/problems/merge-sorted-array/

        Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

        The number of elements initialized in nums1 and nums2 are m and n respectively.
        You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
        Do not return anything, modify nums1 in-place instead.

        """
        i = m-1
        j = n-1
        k = m+n-1

        while k >= 0 and j >= 0 and i >= 0 :
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                # point at i copied. Check next point
                i -= 1
            else:
                nums1[k] = nums2[j]
                # point at j copied. Check next point
                j -= 1
            k -= 1

        # Remaining Elements
        while k >= 0 and i >= 0:
            nums1 [k] = nums1[i]
            k -= 1
            i -= 1
        while j >=0 and k >=0 :
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


pbm = Solution()
nums1 = [1,2,3,9,0,0]
nums2 = [2,6]
m = 4
n = 2
pbm.merge(nums1,m,nums2,n)



