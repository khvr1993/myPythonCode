class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
      """
      Solving using KMP substring match
      if len(s)%(n - longest prefix) == 0 then it can be made
      """