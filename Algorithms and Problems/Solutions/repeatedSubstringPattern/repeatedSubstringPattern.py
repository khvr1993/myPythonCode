class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:
    """
    https://leetcode.com/problems/repeated-substring-pattern/
    Solving using KMP substring match
    if len(s)%(n - longest prefix) == 0 then it can be made
    """

    len_string = len(s)

    # Handle Edge Case
    if len_string < 2:
      return False

    # print(s)
    # print(len_string)
    # Build an array for the string to store the pattern and get longest prefix which is also a suffix

    pre_array = [0 for _ in range(len_string)]

    i = 1
    j = 0
    while i < len_string:
      if s[i] == s[j]:
        j += 1
        pre_array[i] = j
        i += 1
      else :
        # what should be the next value of j
        # Is j at 0?
        if j != 0:
          j = pre_array[j-1]
        else:
          # increment i
          i += 1

    longest_prefix = pre_array[len_string-1]

    print(pre_array)


    if len_string%(len_string-longest_prefix)  == 0 and longest_prefix != 0 :
      return True
    else:
      return False

pbm = Solution()

op = pbm.repeatedSubstringPattern('ab')

print(op)