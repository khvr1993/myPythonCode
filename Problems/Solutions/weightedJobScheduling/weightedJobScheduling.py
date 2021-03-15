class Solution:
  def weightedJobScheduling(self,inp :list) -> int:
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