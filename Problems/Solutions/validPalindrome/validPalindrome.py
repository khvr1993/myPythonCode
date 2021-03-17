class Solution:
    def isPalindrome(self, s: str) -> bool:
      """
      A string is palindrome if it is read the same forwards and backwards
      for i < middle of the string
        A[i] == A[(n-1)-i] n is the length of the string
      """

      # filter returns an iterable for the string. It returns only those characters
      # where str.isalnum is True

      alphanumeric_filter = filter(str.isalnum, s)
      alphanumeric_string = "".join(alphanumeric_filter).casefold()
      # alphanumeric_string = alphanumeric_string_1.casefold()

      # print(alphanumeric_string)

      len_str = len(alphanumeric_string)
      mid = len_str//2
      i = 0
      while i <= mid and len_str > 1:
        if alphanumeric_string[i] != alphanumeric_string[len_str-1-i]:
          isPalindrome = False
          return isPalindrome
        i += 1

      return True


s = Solution()
string = "racea  ; 'car"
op = s.isPalindrome(string)
print(op)