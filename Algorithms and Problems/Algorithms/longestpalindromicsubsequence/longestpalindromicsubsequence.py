from typing import List

def print_table(table : List[int]):
  """Prints the table"""
  for row in table:
    print(row)
  print("------------------------")

class Solution:
  def longestPalindromeSubseq(self,s : str) -> int:
    """
    If the given sequence is “BBABCBCAB”, then the output should be 7 as “BABCBAB” is the longest
    palindromic subsequence in it. “BBBBB” and “BBCBB” are also palindromic subsequences of the
    given sequence, but not the longest ones.
    Important point to note is the letters are not contiguous. This is the main difference between
    longest palindromic substring and subsequence.

    We use dynamic approach to solve this problem
    step1: build a dp_table with the length of the string
    step2: Fill the dp table with 1 in the diagnol
    step3: For the length 2, if s[i] = s[j]  then  1 else 2 (i,j are the position of the charaters in string)
    step4: For strings greater than length 2, if A[i] == A[j] then 2 + dp[i+1,j-1]  (Looking inside)
    step5: If the strings are not equal, if A[i] != A[j] then max(dp[i+1,j], dp[i,j-1]) what is the maximum of not
    including the current character.  eg: comparing [0,4] in BBABCBCAB ` B != C ` => check the max for [1,4]
    BBAB and BABC [0,3]
    """
    # fill_dp_table

    def fill_dp_table(s : str, dp_table : List[int]):
      """
        fills the dp table for length of 1 and 2
      """

      for i in range(len(dp_table)):
        dp_table[i][i] = 1

      # Filling for lengths greater than 0

      row = 0
      col = 1
      while col < len(dp_table):
        if s[row] == s[col]:
          dp_table[row][col] = 2
        else:
          dp_table[row][col] = 1
        row += 1
        col += 1


    length_str = len(s)

    dp_table = [[0 for _ in range(length_str)] for _ in range(length_str)]

    # print_table(dp_table)
    fill_dp_table(s,dp_table=dp_table)

    str_len = 3

    while str_len <= length_str:
      i = 0
      j = i + str_len-1
      str_len += 1

      while j < length_str:
        if s[i] == s[j]:
          dp_table[i][j] =  2 + dp_table[i+1][j-1]

        if s[i] != s[j]:
          dp_table[i][j] = max(dp_table[i+1][j],dp_table[i][j-1])

        j += 1
        i += 1
    # print_table(dp_table)

    return dp_table[0][length_str-1]


s = Solution()
string = "agbdba"
op = s.longestPalindromeSubseq(string)
print(op)






