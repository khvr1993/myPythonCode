class Solution:
  def mindeletions(self,s :str) -> int:
    """
    Return minimum number of deletions required to convert a string to a palindrome.
    This can be solved using longest palindrome sequence.
    Step1: Find the length of the longest palindromic sequence.
    Step2: If we delete the characters which are effecting the longest palindromic sequence the
           string will become palindrome
    """