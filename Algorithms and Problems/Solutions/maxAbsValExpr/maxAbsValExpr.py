from typing import List

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Given two arrays of integers with equal lengths, return the maximum value of:
        |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
        where the maximum is taken over all 0 <= i, j < arr1.length.

        For this we have to utilise the property of modulus
        |x| = x when x >0
            = -x when x < 0

        Upon applying this principle we get 8 different cases like
        Case 1 : arr[i] > arr1[j] , arr2[i] > arr2[j] , i > j
        Case 2: arr[i] < arr1[j] , arr2[i] < arr2[j] , i < j
        Case 3: arr[i] > arr1[j] , arr2[i] < arr2[j] , i > j
        .
        .
        .
        When we evaluate the expressions we reach 4 expressions for which we need to find
        maximum and minimum

        exp1 : arr1[i] + arr2[i] + i
        exp2 : arr1[i] - arr2[i] - i
        exp3 : arr1[i] - arr2[i] + i
        exp4 : arr1[i] + arr2[i] - i

        """

        # Instead of declaring so many variables we can take an array of {1,-1} and {-1,1}
        # cross join it to get 1,1 ; 1-1;-1,1;-1;-1,-1 and get the same expression evaluated
        max_expr1 = -2147483647
        max_expr2 = -2147483647
        max_expr3 = -2147483647
        max_expr4 = -2147483647
        min_expr1 = 2147483648
        min_expr2 = 2147483648
        min_expr3 = 2147483648
        min_expr4 = 2147483648

        length_of_array = len(arr1)

        for i in range(length_of_array):
          max_expr1 = max(max_expr1,(arr1[i] + arr2[i] + i))
          max_expr2 = max(max_expr2,(arr1[i] - arr2[i] - i))
          max_expr3 = max(max_expr3,(arr1[i] - arr2[i] + i))
          max_expr4 = max(max_expr4,(arr1[i] + arr2[i] - i))
          min_expr1 = min(min_expr1,(arr1[i] + arr2[i] + i))
          min_expr2 = min(min_expr2,(arr1[i] - arr2[i] - i))
          min_expr3 = min(min_expr3,(arr1[i] - arr2[i] + i))
          min_expr4 = min(min_expr4,(arr1[i] + arr2[i] - i))

        return max((max_expr1-min_expr1),(max_expr2-min_expr2),(max_expr3-min_expr3),(max_expr4-min_expr4))

pbm = Solution()

arr1 = [1,2,3,4]
arr2 = [-1,4,5,6]

op = pbm.maxAbsValExpr(arr1,arr2)

print(op)
