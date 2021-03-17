from typing import List
class Solution:

	def binarySearch(self,sorted_jobs,start_time) -> int:
		"""
			Performs the binary search and returns the closest job to the current job in question
			which doesnt overlap with the start time of the current job
			sorted_jobs[i][0] => starttime
			sorted_jobs[i][1] => endtime
			sorted_jobs[i][2] => profit

		"""
		lo = 0
		high = start_time-1

		while lo <= high:
			# As long as the lo is greater than high check if the middle element endtime is less than
			# or equal to the start time of the high element
			# If it is less than we see the right side. Looking at the right side because we want to find the
			# closest job which can be used. Since this is iterative we would have calculated the maximum profits
			# for the jobs before start point in earlier iterations and we will use the previously calculated
			# answers
			mid = (lo + high) //2

			if sorted_jobs[mid][1] <= sorted_jobs[start_time][0]:
				# Are there any more jobs to the right of the mid which have their end times
				# less than the start time ?
				if sorted_jobs[mid+1][1] <= sorted_jobs[start_time][0]:
					lo = mid+1
				else:
					return mid
			else:
				high = mid -1

		return -1 # returning -1 indicates that no jobs exist before current job without overlapping




	def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
		"""
			Calculates the optimum Job scheduling and returns the maximum
			pofit.
			1. Weighted Job scheduling is basically selecting the best jobs in a given
				 set of jobs to maximize the profit.
			2. To solve this we use the below approach
			3. First sort the jobs by their finish time
			4. For every job we take the subsets and determine the maximum profit that can be acheived
			5. Here since we can store the profit for every job with other job, we can use dynamic programming
					approach to solve the problem
		"""
		job_schedule = list(zip(startTime,endTime,profit))

		# Sort the array based on finish time

		sorted_jobs = sorted(job_schedule,key= lambda x:x[1])

		# Declare a table with the length of the list to store the profits

		profit_table = [0 for _ in range(len(sorted_jobs))]

		# For the first job the profit will always be the first jobs profit only

		profit_table[0] = sorted_jobs[0][2]

		""" Starting from the second job we need to find out the maximum profit
				For this what we need to see what is the profit if we pick the current job
				and what would be the profit if we dont pick the current job
				Which ever is maximum that will be the profit that will be taken
				profit_table[i] = MAX(Profit[i],profit_table[i-1])
		"""

		for index in range(1,len(sorted_jobs)):
			# Profit for second job is profit of the second job + Are there any jobs prior to the
			# current job which can be picked

			non_overlapping_job = self.binarySearch(sorted_jobs,index)

			if non_overlapping_job != -1 : # Some job exists before current job which is not overlapping
				profit_non_overlapping_job = profit_table[non_overlapping_job]
			else:
				profit_non_overlapping_job = 0

			# print(f"profit from non overlapping job {profit_non_overlapping_job}")

			profit = sorted_jobs[index][2] + profit_non_overlapping_job

			profit_table[index] = max(profit,profit_table[index-1])


		# print(profit_table)


		return profit_table[-1]







s = Solution()
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
op = s.jobScheduling(startTime=startTime,endTime=endTime,profit=profit)
print(op)
