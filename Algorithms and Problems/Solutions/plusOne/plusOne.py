from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/plus-one/
        Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

        The digits are stored such that the most significant digit is at the head of the list,
        and each element in the array contains a single digit.

        You may assume the integer does not contain any leading zero, except the number 0 itself.

        We have to iterate the list from the ending. and only if there is a carry we need to move forward
        """
        sum = 0
        carry = 0
        length_of_list = len(digits)
        while length_of_list > 0:
            carry = 0
            sum = digits[length_of_list-1] + 1 # Loop running second time => add carry and carry cannot be greater than 1
            if sum > 9 :
                carry = 1
                sum = sum % 10

            digits[length_of_list-1] = sum

            # No Carry Received exit the loop
            if carry == 0:
                break

            length_of_list -= 1

            # first element in the list processed, a carry is there and the remainder was 0
            if length_of_list == 0 and carry == 1 :
                digits.insert(0,1)

        return digits

pbm = Solution()
digits = [8,9,9,9]
op = pbm.plusOne(digits)
print(op)



