from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadanes Algorithm
        to include or not to include the element
        """
        currentSubArraySum = nums[0]
        maxSubArraySum = nums[0]

        for i in range(1,len(nums)):
            # include current element and see if if we have maximum or we need to start from the current element
            currentSubArraySum = max(currentSubArraySum+nums[i],nums[i])
            # is the currencysubarraysum the maximum
            maxSubArraySum = max(currentSubArraySum,maxSubArraySum)

        return maxSubArraySum

pbm = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
op = pbm.maxSubArray(nums)
print(op)
