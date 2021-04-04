from typing import List

class Solution:
  def maxAbsoluteDiff(self,x :List[int]) -> int:
    """
    Given an unsorted array A of N integers, A_{1}, A_{2}, ...., A_{N}.
    Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
      f(i, j) or absolute difference of two elements of an array A is defined as
      |A[i] – A[j]| + |i – j|, where |A| denotes
      the absolute value of A.

    Solution :
    1. For Brute force calculate all the pairs and maintain a maximum value and return it
    2. For O(n) approach, it is a tricck question
       we have to use the modulus functionality
       |x| = x if x > 0
           = -x if x < 0

    Now consider the below cases

      A[i] > A[j] and i>j. Both the modulus are positive. So we get
      A[i] - A[j] + i - j
      => (A[i]+i) - (A[j]+j)
      ===========================
      Similarly for other cases
      A[i] < A[j] and i < j
      => -(A[i]+i) + (A[j]+j)
      ===========================
      A[i] < A[j]  and i > j
      -A[i]+A[j] + i - j
      (-A[i]+i) - (-A[j] +j)
      ===========================
      A[i] > A[j] i < j
      A[i] - A[j] -i + j
      -(-A[i]+i) + (-A[j]+j)
      ===========================

      For two A - B to be maximum we can take max of A - min B

      So we find
      MAX(A[i]+i)
      MIN(A[i]+i)
      MAX(i-A[i])
      MIN(i-A[i])

    """
    length_of_array = len(x)
    max1 = -2147483647
    max2 = -2147483647
    min1 = 2147483648
    min2 = 2147483648
    for i in range(length_of_array):
      max1 = max(max1,(x[i]+i))
      min1 = min(min1,(x[i]+i))
      max2 = max(max2,(i-x[i]))
      min2 = min(min2,(i-x[i]))

    return max((max1-min1),(max2-min2))

pbm = Solution()
x = [-1,-3,1]
op = pbm.maxAbsoluteDiff(x)
print(op)
