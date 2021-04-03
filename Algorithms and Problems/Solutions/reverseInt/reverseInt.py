class Solution:
		def reverse(self, x: int) -> int:
				"""
				https://leetcode.com/problems/reverse-integer/
				Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

				Solution Maximum Value and Minimum Value
				Maximum Value = 2147483648
				Minimum Value = -2147483647

				In python modulo operator  mod = n - math.floor(n/base) * base
				"""
				rev = 0
				MAX_VALUE = 2147483648
				MIN_VALUE = -2147483647
				x_post = True if x >= 0 else False

				x = abs(x)

				while x != 0:
					remainder = x%10
					x //= 10
					print(f"reverse {rev} max allowed value {MAX_VALUE//10} current value of x {x}")
					if (rev*(1 if x_post else -1) > MAX_VALUE//10
							or (rev*(1 if x_post else -1) == MAX_VALUE//10 and remainder > 7 )):
							return 0
					if (rev*(1 if x_post else -1) < MIN_VALUE//10
							or (rev*(1 if x_post else -1) == MIN_VALUE//10 and remainder > -8) ):
						return 0
					rev = rev*10  + remainder
				return rev*(1 if x_post else -1)


pbm = Solution()
x= -1
op = pbm.reverse(x)
print(op)


