class Solution:
	def kmp(self,s ,pattern) :
		"""
		https://www.youtube.com/watch?v=KG44VoDtsAA

		Knuth Moris Pratt algorithm works on the concept of prefix and suffix

		Consider a string abcdabc
		prefix for this strings are: a,ab,abc,abcd
		suffix for this strings are: c,bc,abc,dabc,cdabc,bcdabc

		Is there any string which is a prefix as well as a suffix. This knowledge
		is used so that when comparing we dont lose the progress which is the main
		problem in the brute force approach

		Step 1: we build a pi table for the pattern. This involves we assigning the positions
		the tracker to be returned to when a match is not found. The length of the array will be
		len(pattern) + 1

		Step 2: Position tracker i in the string and j in the pattern string at 0 and start comparing
		when a match is found then increment botth i and j.
		Step3: When a match is not found then move the position of j to the index of the element present in
		the pi table at j
		Step 4: When a match is not found still at the index of the table move the position of the i to the
		next val

		"""
		# create pi table

		print(pattern)
		len_pattern = len(pattern)

		print(f"length of pattern {len_pattern}")

		pi_table = [0 for _ in range(len_pattern) ]

		print(pi_table)

		# build the pi_table with the correct indices
		i = 1
		j = 0

		while i < len_pattern:
			# If the value at i and j are equal then we increment the value of i and j and
			# store the value in the pi_table.
			# This means that in the string with length of 0 to i, there is a prefix of length
			# j which is also a suffix
			# aab a at position 1 is a prefix as well as suffix

			if pattern[i] == pattern[j]:
				j += 1
				pi_table[i] = j # length of the string
				i += 1
			else:
				# move the position of j to the position present in the pi table[j-1]
				# if the j position is already at 0 then increment i
				# We are doing to see what is the length of the string which is a prefix as
				# well as suffix
				# for eg in acacabacacabacacac acac at the end is prefix as well as suffix a
				if j != 0:
					j = pi_table[j-1]
				else:
					i += 1

		print(pi_table)
		return True

kmp = Solution()
s = 'THIS IS A TEST TEXT'
pattern = 'acacabacacabacacac'
op = kmp.kmp(s,pattern=pattern)


