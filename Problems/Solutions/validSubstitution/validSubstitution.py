#https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
class Solution:
		def isValid(self, s: str) -> bool:
			"""
				Returns whether the str is eligible for valid substitution
				Check initial conidtions.
				Always the first and last elements should be a and c drespectively.
				if Not return false
				if the length of the string is < 3 return false
				initialise an array.
				In a loop traverse through the string and keep inserting the values.
				When we encounter the letter c POP the elements and check whether we are getting b and a
			"""
			if len(s) < 3 or s[0] != 'a' or s[-1] != 'c' or len(s)%3 != 0 :
				return False

			stack = []
			# print(s)
			for letters in s:
				stack.append(letters)
				if letters == 'c':
					# pop the inserted c element
					stack.pop()
					if len(stack) == 0 or stack.pop() != 'b':
						return False
					if len(stack) == 0  or stack.pop() != 'a':
						return False

			return True


s = Solution()
val = s.isValid("abcbcababcabbbcbbc")
print(val)