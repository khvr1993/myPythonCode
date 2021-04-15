class Solution:
    def climbStairs(self, n: int) -> int:
        """
        https://leetcode.com/problems/climbing-stairs/

        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        Solution:
        Can be solved using recursive approach
        Exit condition : n = 1,n = 2
        we can use memoization to reduce the calculations by storing the calculated values

        Alternate way is to use DP Approach

        """
        # build dynamic table
        if n == 0 :
            return 0
        elif n == 1:
            return 1
        dp_table = [0 for _ in range(n+1)]
        print(dp_table)
        dp_table[1] = 1
        dp_table[2] = 2
        for i in range(3,n+1):
            dp_table[i] = dp_table[i-1] + dp_table[i-2]

        return dp_table[n]

pbm = Solution()
n = 3
op = pbm.climbStairs(n)
print(op)