class Solution:

  def longestcommonsubsequence_recursion(self,string_1 :str,string_2 :str) -> int:
    """
    Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”

    when finding common substrings we do the following actions
    acefg    -> A
    abcdefg  -> B

    start with A[i] = 0 and B[j] = 0
    if A[i] and B[j] are equal then a is a subsequence and we increment both i and j
    Compare A[i+1] and B[j+1] again now if both are not equal then increment any one of i
    or j(Both needs to be done and maximum needs to be checked) and start the comparision.
    As and when they are equal we need to move the positions forward while increasing the length.

    Algorithm for recursion is

    If i or j reaches the end of the string return 0 --> Terminating condition
    If A[i] == A[j] then return 1 + lcs(i+1,j+1) --> Incrementing condition and recursion

    If A[i] != A[j] then return Max(lcs(i+1,j) || lcs(i,j+1) ) --> recursion getting called here

    """

    len_string1 = len(string_1)
    len_string2 = len(string_2)
    match = []


    def lcs(i :int,j: int ) -> int:
      """
      recursion approach to calculate the longest common subsequence
      """
      # print("----------")
      # print(f"Parameters i = {i} j = {j} ")

      if i == len_string1  or j == len_string2 : #Exit Condition ANy string end reached
        return 0

      # print(f"String value is {string_1[i]} and {string_2[j]}")


      if string_1[i] == string_2[j]:
        # print("incrementing size by 1")
        return 1 + lcs(i+1,j+1)

      if string_1[i] != string_2[j]:
        # print("Call recursion")
        return max(lcs(i+1,j),lcs(i,j+1))

    longest_subsequence = lcs(0,0)

    return longest_subsequence



s= Solution()
string_1 = "AGT"
string_2 = "GXT"
op = s.longestcommonsubsequence_recursion(string_1,string_2)

print(op)
