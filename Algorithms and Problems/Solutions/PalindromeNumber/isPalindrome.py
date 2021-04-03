class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        https://leetcode.com/problems/palindrome-number/
        Given an integer x, return true if x is palindrome integer.

        An integer is a palindrome when it reads the same backward as forward.
        For example, 121 is palindrome while 123 is not.

        Solution:
        All negative integers are not palindrome
        All integers divisible by 10 are not palindrome
        if the reversed integer is overflowing that means that the x is not palindrome
        """
        rev = 0
        MAX_VALUE = 2147483648
        original_value = x

        if (x < 0 or (x%10 == 0 and x > 9 )):
          return False

        while (x != 0):
          # print(f"reverse {rev} max allowed value {MAX_VALUE//10} current value of x {x}")

          remainder = x%10
          x //= 10
          if (rev > MAX_VALUE//10):
            return False

          rev = rev*10 + remainder

        # print(f"Reversed int {rev} and x is {original_value}")
        if rev == original_value:
          return True

pbm = Solution()
x = 1
op = pbm.isPalindrome(x)
print(op)

