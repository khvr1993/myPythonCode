class Solution:
    def mySqrt(self, x: int) -> int:
        """
        https://leetcode.com/problems/sqrtx/

        Given a non-negative integer x, compute and return the square root of x.

        Since the return type is an integer,
        the decimal digits are truncated, and only the integer part of the result is returned.

        Solution :
        We have math.sqrt but using this is not intended.

        From 1 .. n we find the square of each number and see what is the closest number to the given number and return

        For small numbers this is fine but for large numbers this is not desirable.
        We have to skip some computations to make program run faster.

        Property of square root
        sqrt(n) >= n/2 except for 1

        we can uses binary search to minimise the computations
        """
        if x == 0:
            return 0
        elif x == 1:
            return 1

        min_diff = 2147483647

        def binary_search_sqt(start,end,target) -> int:
            """
            performs binary search to find the sqrt and return the value closest to sqrt
            """
            print(f"start {start} end {end} target {target}")
            if start > end:
                return end
            while start <= end:
                mid = (start+end)//2
                # if target-mid*mid > min_diff:
                #     return mid-1
                if (mid*mid) == target:
                    return mid
                elif (mid*mid) > target:
                    # min_diff = min(min_diff,target-mid^2)
                    return binary_search_sqt(start,mid-1,target)
                elif (mid*mid) < target:
                    # min_diff = min(min_diff,target-mid^2)
                    return binary_search_sqt(mid+1,end,target)


        op = binary_search_sqt(0,x,x)
        return op

pbm = Solution()
x = 99
op = pbm.mySqrt(x)
print(op)