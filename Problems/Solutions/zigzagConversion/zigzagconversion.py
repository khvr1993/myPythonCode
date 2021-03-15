class Solution:
	def convert(self, s: str, numRows: int) -> str:
		"""
		returns the zigzag string without formatting
		"""
		# Initially we take the string and traverse row wise and insert into the
		# first column. Once you reach the end then we change the direction of the
		# insertion and also insert into the second column. Again when we reach the top
		# change the direction again .
		# PAHN
		# APLSIIG
		# YIR

		# Create a row matrix with the numRows
		# start appending data into the matrix

		# Only one row implies everything will be inserted in the orderly fashion
		if numRows == 1 or len(s) <= numRows:
			return s

		charArray = [[] for _ in range(numRows)]

		row = 0
		direction = -1
		returnVal = ''

		for letters in s:
			charArray[row].append(letters)
			if row == (numRows-1) or row == 0:
				# change the direction
				direction *= -1
			row += direction

		for row in charArray:
			returnVal += ''.join(row)

		return returnVal



string = 'PAYPALISHIRING'
s = Solution()
Solution.convert(s,string,3)
