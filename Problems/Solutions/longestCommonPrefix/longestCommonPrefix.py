from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      """
      https://leetcode.com/problems/longest-common-prefix/

      Write a function to find the longest common prefix string amongst an array of strings.

      If there is no common prefix, return an empty string "".

      """

      op = []
      is_a_prefix = True

      if len(strs) == 0 :
        return ""

      for i in range(len(strs[0])): # First letter picked
        j = 1
        prefix_comparision_letter = strs[0][i]

        if not(is_a_prefix):
          break;

        # print(prefix_comparision_letter)

        while j < len(strs):# for all the strings

          # print(f"Value of i is {i} prefix_comparision_letter = {prefix_comparision_letter} value of j is {j}")

          length_of_compare_string = len(strs[j])

          # This is return to exit when the index of first element letters are greater than the letters being compared
          # meaning all the letters in the string are complete. That is the longest prefix

          if i >= length_of_compare_string:
            return "".join(op)

          # If any string is having not letters then longest prefix is ""
          if length_of_compare_string == 0 :
            return ""

          if strs[j][i] != prefix_comparision_letter:
            is_a_prefix = False
            break;

          j += 1

        # For all the letters present
        if (is_a_prefix) :
          op.append(prefix_comparision_letter)

      return "".join(op)

pbm = Solution()
strs =  ["flower","flow","flight"]
op = pbm.longestCommonPrefix(strs)

print(op)

