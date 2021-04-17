from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/next-greater-element-i/

        Solution :
        To find the next greater element we can just look at the nums2 array and find the next
        greatest element for every element.
        The process to find this is
        1. we insert the first element into the stack
        2. if the top element in the stack is greater than the current element then
            insert into the stack
        3. If the current element is greater than the top of the stack make a map
            such that the key is the top of the stack and the current element is the value
        [7,4,1,3,6]
        stack operations
        insert 4
        insert 1
        pop 3 [ 1 => 3 ]
        insert 3
        pop 3 [3=>6]
        insert 6
        pop 6 [4 => 6]
        if stack is not empty then mark -1

        """
        gt_dict = {}
        stack = []
        output =[]

        # use nums2 since nums1 is the subset
        for value in nums2:
            # If the current element is less than the previous element then we need to move forward to get the next greatest element
            while len(stack) > 0 and stack[-1] < value:
                #Capturing the next greatest element
                gt_dict[stack.pop()] = value
            #Add to the stack the lesser element [This will allow us to get the greatest element for the inserted element]
            stack.append(value)
        print(f"stack {stack} gt_dict {gt_dict}")

        # Map the remaining elements in stack to -1
        for value in stack:
            gt_dict[value] = -1
        print(f"stack {stack} gt_dict {gt_dict}")

        for value in nums1:
            output.append(gt_dict[value])

        return output


pbm = Solution()
nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
op = pbm.nextGreaterElement(nums1,nums2)
print(op)
