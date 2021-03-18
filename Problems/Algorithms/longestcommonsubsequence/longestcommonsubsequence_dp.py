from typing import List

class Solution:


  def longestcommonsubsequence_dp(self,string_1 :str,string_2 :str) -> int:
    """
    Given two sequences, find the length of longest subsequence present in both of them.
    A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
    For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”

    For DP
    step1: Create an array with len(string 1)+1 as rows and len(string 2)+1 as columns.
    step2: Fill the dp array with 0 for the first row and first column
    step3: DP Table is filled top to bottom. We use the calculated data in the next calculation
    step4: Get the value of the last row and last column and that is the length of the longest common subsequence

    Formula for DP is
    if string[i] == string[j] 1+ DP(i-1,j-1) [adding the diagnol element looking backwards]
    if string[i] != string[j] MAX(DP(i-1,j), DP(i,j-1)) [ Looking at the column on top and row on the Left hand side]
    """

    len_string1 = len(string_1)
    len_string2 = len(string_2)

    # Creating the dp table
    dp_table = [['' for _ in range(len_string2+1) ] for _ in range(len_string1+1)]
    start = 1

    # filling first row and column with 0

    for i in range(len_string2+1):
      dp_table[0][i] = 0

    for j in range(len_string1+1):
      dp_table[j][0] = 0


    printtable(dp_table)

    for i in range(len_string1):

      end = 1

      for j in range(len_string2): # for every row navigate through the columns

        # print(f"The value of start is {start} and end is {end}")

        if end > len_string2+1:
          break

        if string_1[i] == string_2[j]:
          dp_table[start][end] = 1 + dp_table[start-1][end-1]

        if string_1[i] != string_2[j]:
           dp_table[start][end] = max(dp_table[start-1][end],dp_table[start][end-1])

        end += 1
      start += 1

    return dp_table


def printtable(table : List[int]):
  """Prints the table"""
  for row in table:
    print(row)

  print(' ')

def trace_subsequence(string_1 :str,string_2 :str,dp_table : List[int]) -> str:
  """
    This will trace the dp_table and returns the subsequence which is the longest
  """
  rows = len(dp_table) - 1
  cols = len(dp_table[0]) - 1
  longest_subs = []

  while cols > 0 :
    print(f"Looking into row {rows} and cols {cols}")
    if dp_table[rows-1][cols] ==  dp_table[rows][cols-1] :

      # Check if current cell is having a value greater than zero. This is required because having 1 => substring was found
      if dp_table[rows][cols] != 0 :
        longest_subs.append(string_2[cols-1])

      #move diagnol
      cols -= 1
      rows -= 1

      print(longest_subs)

    else:
      dp_table[rows-1][cols] !=  dp_table[rows][cols-1]
      #move left
      cols -= 1



  return longest_subs


# ==========================================
s = Solution()
string_1 = "stone"
string_2 = "longest"
op = s.longestcommonsubsequence_dp(string_1,string_2)
printtable(op)

print(f"The size of the longest common subsequence is {op[len(string_1)][len(string_2)]}")

trace_subsequence(string_1,string_2,op)



