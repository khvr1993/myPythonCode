from typing import List

def print_table(table : List[int]):
  """Prints the table"""
  for row in table:
    print(row)
  print("------------------------")

class Solution:

  def init_dp_table(self,s,lps_dp_table,len_string):
    """
      Fills the dp table for lengths of 1 and 2
    """
    # Filling for length 1
    for i in range(len_string):
      lps_dp_table[i][i] = 1

    j = 1
    i = 0

    # Filling for length 2
    while j < len_string:

      if s[i] == s[j]:
        lps_dp_table[i][j] = 2
      else:
        lps_dp_table[i][j] = 1

      i += 1
      j += 1



  def mindeletions(self,s :str) -> int:
    """

    https://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/

    Return minimum number of deletions required to convert a string to a palindrome.
    This can be solved using longest palindrome subsequence.
    Step1: Find the length of the longest palindromic subsequence.
    Step2: If we delete the characters which are effecting the longest palindromic subsequence the
           string will become palindrome
    """
    len_string = len(s)
    lps_dp_table = [[0 for _ in range(len_string)] for _ in range(len_string)]
    print_table(lps_dp_table)

    self.init_dp_table(s,lps_dp_table,len_string)

    print_table(lps_dp_table)

    # For lengths greater than 2
    length = 3

    while length <= len_string:
      i = 0
      j = i + length -1
      while j < len_string:

        print(f"value of i is {i} and value of j is {j}")
        if s[i] == s[j]:
          lps_dp_table[i][j] = 2 + lps_dp_table[i+1][j-1] # Looking inside
          j += 1
          i += 1
        else:
          lps_dp_table[i][j] = max(lps_dp_table[i+1][j],lps_dp_table[i][j-1])
          j += 1
          i += 1
      length += 1

    print_table(lps_dp_table)

    return len_string - lps_dp_table[0][len_string-1]




pbm = Solution()
string = 'geeksforgeeks'
op = pbm.mindeletions(string)
print(op)