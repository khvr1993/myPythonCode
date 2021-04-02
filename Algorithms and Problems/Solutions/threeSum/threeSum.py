from typing import List

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		"""
		https://leetcode.com/problems/3sum/

		Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

		Notice that the solution set must not contain duplicate triplets.

		Solution :
			1. First sort the array
			2. for every element we need to find the other 2 elements where the sum is the
					opposite of the selected element
		"""

		nums = sorted(nums)
		op_list = []

		print(nums)

		length_of_nums = len(nums)

		if length_of_nums < 3:
			return []

		for elems in range(0,length_of_nums-2):
			"""
				for the selected element find the other 2 elements
			"""

			# print(elems)

			if nums[elems] == nums[elems-1] and elems > 0:
				continue;

			first_val =  nums[elems]
			low = elems+1
			high = length_of_nums-1


			while low < high :

				# print(f"low = {low} high = {high} elem = {elems}")

				second_val = nums[low]
				third_val = nums[high]

				if second_val + third_val + first_val > 0:
					# if the next elements are same then to avoid duplicates skip that element
					if nums[high-1] == third_val:
						high -= 2
						while low < high  and  (nums[high] == third_val):
							high -= 1
					else:
						high -=1
					# if the next elements are same then to avoid duplicates skip that element
				elif (second_val + third_val + first_val) < 0:
					if second_val == nums[low+1]:
						low +=2
						while low < high  and second_val == nums[low]:
							low += 1
					else:
						low += 1
					# if the next elements are same then to avoid duplicates skip that element
				else:
					# print("Found Zero")
					op_list.append([first_val,second_val,third_val])
					if  second_val == nums[low+1]:
						low += 2
						while low < high and second_val == nums[low]:
							low += 1
					else:
						low += 1

		return op_list

pbm = Solution()
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

op_list = pbm.threeSum(nums)

print(op_list)

# [-4, -1, -1, 0, 1, 2]
# [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

