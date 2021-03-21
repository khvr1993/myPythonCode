from collections import Counter
class Solution:
  def longestPalindrome(self, s: str) -> int:
    """
      Returns the longest palindrome possible with the given characters
    """

    #building a dictionary with the count of letters
    s_dict = Counter(s)
    len_string = len(s)
    print(s_dict)

    longest_palindrome = 0
    for key,values in s_dict.items():
      # palindrome has repeating characters
      longest_palindrome += (values//2)*2
      print(f"Longest palindrome for letter {key} is {longest_palindrome}")

    # if given length of string is odd then add one else return the longest palindrome

    if (len_string - longest_palindrome) != 0:
      return longest_palindrome+1
    else :
      return longest_palindrome


pbm = Solution()
string = 'abba'
op = pbm.longestPalindrome(string)
print(op)
